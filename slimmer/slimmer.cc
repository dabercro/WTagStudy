#include <algorithm>
#include <iostream>
#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"
#include "TH1F.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TF1.h"
#include "TMath.h"

#include "KinematicFunctions.h"
#include "OutTree.h"
#include "NeroTree.h"

enum IsoType {
  kIsoVeto = 0,  
  kIsoLoose,
  kIsoMedium,
  kIsoTight  
};

Bool_t PassIso(Float_t lepPt, Float_t lepEta, Float_t lepIso, Int_t lepPdgId, IsoType isoType) {

  Float_t isoCut = 0.;

  if (abs(lepPdgId) == 13) {
    isoCut = (isoType == kIsoTight) ? 0.12 : 0.20;
  }
  else {
    switch (isoType) {
    case kIsoVeto:
      isoCut = (fabs(lepEta) <= 1.479) ? 0.126 : 0.144;
      break;  
    case kIsoLoose:
      isoCut = (fabs(lepEta) <= 1.479) ? 0.0893 : 0.121;
      break;
    case kIsoMedium:
      isoCut = (fabs(lepEta) <= 1.479) ? 0.01603226 : 0.0678;
      break;
    case kIsoTight:
      isoCut = (fabs(lepEta) <= 1.479) ? 0.0354 : 0.0646;
      break;
    default:
      break;
    }
  }
  return (lepIso/lepPt) < isoCut;
}

void slimmer(TString inFileName, TString outFileName, Bool_t isSig = false) {

  Float_t dROverlap  = 0.4;
  Float_t dRGenMatch = 0.2;
  Float_t bCutLoose  = 0.605;
  Float_t bCutMedium = 0.89;
  Float_t bCutTight  = 0.97;

  TFile *outFile = new TFile(outFileName,"RECREATE");
  OutTree *outTree = new OutTree("events", outFile);
  TH1F *allHist = new TH1F("htotal","htotal",1,-1,1);

  TFile *inFile           = TFile::Open(inFileName);
  TTree *inTreeFetch      = (TTree*) inFile->Get("nero/events");
  NeroTree *inTree  = new NeroTree(inTreeFetch);
  TTree *allTree          = (TTree*) inFile->Get("nero/all");
  Float_t mcWeight        = 0.;
  TBranch *mcWeightBranch = allTree->GetBranch("mcWeight");
  mcWeightBranch->SetAddress(&mcWeight);

  TLorentzVector vec1;
  TLorentzVector vec2;
  TLorentzVector vec3;

  TLorentzVector saveGenVec;
  TLorentzVector saveDMVec;

  Int_t nentries = inTreeFetch->GetEntriesFast();

  std::vector<TLorentzVector*> leptonVecs;
  std::vector<TLorentzVector*> photonVecs;

  Float_t checkDR = 0.0;
  
  for (Int_t iEntry = 0; iEntry < allTree->GetEntriesFast(); iEntry++) {
    mcWeightBranch->GetEntry(iEntry);
    if (mcWeight > 0)
      allHist->Fill(0.0,1.0);
    else if (mcWeight < 0)
      allHist->Fill(0.0,-1.0);
  }

  outFile->WriteTObject(allHist,allHist->GetName());

  for (Int_t iEntry = 0; iEntry < nentries; iEntry++) {
    
    //// Clear out the saved vectors for cleaning ////

    leptonVecs.resize(0);
    photonVecs.resize(0);

    if (iEntry % 10000 == 0)
      std::cout << "Processing events: ... " << float(iEntry)/float(nentries)*100 << "%" << std::endl;
    
    inTree->GetEntry(iEntry);
    
    //// Fill some global event values ////

    outTree->runNum    = inTree->runNum;
    outTree->lumiNum   = inTree->lumiNum;
    outTree->eventNum  = inTree->eventNum;
    outTree->npv       = inTree->npv;
    outTree->npvTrue   = inTree->puTrueInt;
    outTree->rho       = inTree->rho;

    if (isSig)
      outTree->mcWeight = inTree->mcWeight;
    else {
      if (inTree->mcWeight < 0)
        outTree->mcWeight = -1;
      else
        outTree->mcWeight = 1;
    }

    outTree->met    = ((TLorentzVector*)((*(inTree->metP4))[0]))->Pt();
    outTree->metPhi = ((TLorentzVector*)((*(inTree->metP4))[0]))->Phi();

    outTree->triggerFired = inTree->triggerFired;
    
    //// Here is the lepton filling ////

    for (Int_t iLepton = 0; iLepton < inTree->lepP4->GetEntries(); iLepton++) {
      TLorentzVector* tempLepton = (TLorentzVector*) inTree->lepP4->At(iLepton);
      
      //// Rejecting leptons with Eta cuts ////

      if ((fabs(tempLepton->Eta()) > 2.5) ||
          (fabs(tempLepton->Eta()) > 2.4 && fabs((*(inTree->lepPdgId))[iLepton]) == 13))
        continue;

      //// Filling lepton values based on loose cut for muons and veto cut for electrons ////

      if (tempLepton->Pt() > 10. && (
          ( fabs((*(inTree->lepPdgId))[iLepton]) == 13 && ((*(inTree->lepSelBits))[iLepton] & 16) == 16 &&
            PassIso(tempLepton->Pt(),tempLepton->Eta(),(*(inTree->lepIso))[iLepton],(*(inTree->lepPdgId))[iLepton],kIsoLoose)
          ) ||
          (fabs((*(inTree->lepPdgId))[iLepton]) == 11 && ((*(inTree->lepSelBits))[iLepton] & 2) == 2 &&
            PassIso(tempLepton->Pt(),tempLepton->Eta(),(*(inTree->lepIso))[iLepton],(*(inTree->lepPdgId))[iLepton],kIsoVeto)
          )  
          )) {

        outTree->n_looselep++;
        if (outTree->n_looselep == 1) {
          outTree->lep1Pt    = tempLepton->Pt();
          outTree->lep1Eta   = tempLepton->Eta();
          outTree->lep1Phi   = tempLepton->Phi();
          outTree->lep1PdgId = (*(inTree->lepPdgId))[iLepton];
          outTree->lep1IsMedium = 0;
          outTree->lep1IsTight  = 0;
          outTree->lep1RelIso = (*(inTree->lepIso))[iLepton]/outTree->lep1Pt;
        }          
        else if (outTree->n_looselep == 2) {
          outTree->lep2Pt    = tempLepton->Pt();
          outTree->lep2Eta   = tempLepton->Eta();
          outTree->lep2Phi   = tempLepton->Phi();
          outTree->lep2PdgId = (*(inTree->lepPdgId))[iLepton];
          outTree->lep2IsMedium = 0;
          outTree->lep2IsTight  = 0;
          outTree->lep2RelIso = (*(inTree->lepIso))[iLepton]/outTree->lep2Pt;
        }          

        if (tempLepton->Pt() > 20. && ((*(inTree->lepSelBits))[iLepton] & 32) == 32 &&
            PassIso(tempLepton->Pt(),tempLepton->Eta(),(*(inTree->lepIso))[iLepton],(*(inTree->lepPdgId))[iLepton],kIsoMedium)) {

          outTree->n_mediumlep +=1;
          if (outTree->n_looselep == 1)
            outTree->lep1IsMedium = 1;
          else if (outTree->n_looselep == 2)
            outTree->lep2IsMedium = 1;
        }

        //// We are cleaning tight leptons from jets ////

        if (tempLepton->Pt() > 20. && ((*(inTree->lepSelBits))[iLepton] & 64) == 64 &&
            PassIso(tempLepton->Pt(),tempLepton->Eta(),(*(inTree->lepIso))[iLepton],(*(inTree->lepPdgId))[iLepton],kIsoTight) &&
            (abs((*(inTree->lepPdgId))[iLepton]) == 13 || tempLepton->Pt() > 40.)) {

          leptonVecs.push_back(tempLepton);
          outTree->n_tightlep +=1;
          if (outTree->n_looselep == 1)
            outTree->lep1IsTight = 1;
          else if (outTree->n_looselep == 2)
            outTree->lep2IsTight = 1;
        }
      }
    }
    
    //// If there are identified leptons, we will define our recoil using them ////

    if (outTree->n_looselep > 0)
      outTree->mt = transverseMass(outTree->lep1Pt, outTree->lep1Phi, outTree->met, outTree->metPhi);
    
    //// Now we go on to look at photons ////
    
    for (Int_t iPhoton = 0; iPhoton < inTree->photonP4->GetEntries(); iPhoton++) {
      TLorentzVector* tempPhoton = (TLorentzVector*) inTree->photonP4->At(iPhoton);
      
      //// Set photon cuts at some pt and eta ////

      if (tempPhoton->Pt() < 15. || fabs(tempPhoton->Eta()) > 2.5 || 
          ((*(inTree->photonSelBits))[iPhoton] & 8) != 8)
        continue;

      outTree->n_loosepho++;

      //// Usign the medium photon collection for futher cleaning ////
      if (tempPhoton->Pt() > 175 && ((*(inTree->photonSelBits))[iPhoton] & 16) == 16) {
        photonVecs.push_back(tempPhoton);
        outTree->n_mediumpho++;
      }
      
      if (outTree->n_loosepho == 1) {
        outTree->pho1Pt    = tempPhoton->Pt();
        outTree->pho1Eta   = tempPhoton->Eta();
        outTree->pho1Phi   = tempPhoton->Phi();
        if (outTree->n_mediumpho == 1)
          outTree->pho1IsMedium = 1;
        else
          outTree->pho1IsMedium = 0;
      }
      if (outTree->n_loosepho == 2) {
        outTree->pho2Pt    = tempPhoton->Pt();
        outTree->pho2Eta   = tempPhoton->Eta();
        outTree->pho2Phi   = tempPhoton->Phi();
        if (outTree->n_mediumpho == 1)
          outTree->pho2IsMedium = 1;
        else
          outTree->pho2IsMedium = 0;
      }
    }
    
    Double_t checkDPhi = 5.0;
    Double_t clean_checkDPhi = 5.0;

    for (Int_t iJet = 0; iJet < inTree->jetP4->GetEntries(); iJet++) {
      TLorentzVector* tempJet = (TLorentzVector*) inTree->jetP4->At(iJet);
      
      //// Ignore jets that are not in this region ////
      if (fabs(tempJet->Eta()) > 2.4 || (*(inTree->jetPuId))[iJet] < -0.62 || tempJet->Pt() < 30.0)
        continue;

      outTree->n_jets++;

      //// Now do cleaning ////
      
      Bool_t match = false;
      
      for (UInt_t iLepton = 0; iLepton < leptonVecs.size(); iLepton++) {
        if (deltaR(leptonVecs[iLepton]->Phi(),leptonVecs[iLepton]->Eta(),tempJet->Phi(),tempJet->Eta()) < dROverlap) {
          match = true;
          break;
        }
      }
      
      if (match)
        continue;
      
      for (UInt_t iPhoton = 0; iPhoton < photonVecs.size(); iPhoton++) {
        if (deltaR(photonVecs[iPhoton]->Phi(),photonVecs[iPhoton]->Eta(),tempJet->Phi(),tempJet->Eta()) < dROverlap) {
          match = true;
          break;
        }
      }
      
      if (match)
        continue;
      
      //// Count jets for b-tagging ////

      float dR_1 = dROverlap + 0.1;
      float dR_2 = dROverlap + 0.1;

      if (outTree->lep1Pt > 0)
        dR_1 = deltaR(outTree->lep1Phi, outTree->lep1Eta, tempJet->Phi(),tempJet->Eta());
      if (outTree->lep2Pt > 0)
        dR_2 = deltaR(outTree->lep2Phi, outTree->lep2Eta, tempJet->Phi(),tempJet->Eta());

      if (dR_1 > dROverlap && dR_2 > dROverlap) {
        if ((*(inTree->jetBdiscr))[iJet] > bCutTight)
          outTree->n_bjetsTight++;
        if ((*(inTree->jetBdiscr))[iJet] > bCutMedium)
          outTree->n_bjetsMedium++;   
        if ((*(inTree->jetBdiscr))[iJet] > bCutLoose)
          outTree->n_bjetsLoose++;
        else          // Only want to save the first two b-tagged jets
          continue;
      }
      
      if (outTree->n_bjetsLoose == 1) {
          outTree->bjet1Pt   = tempJet->Pt();
          outTree->bjet1Eta  = tempJet->Eta();
          outTree->bjet1Phi  = tempJet->Phi();
          outTree->bjet1M    = tempJet->M();
          outTree->bjet1BTag = (*(inTree->jetBdiscr))[iJet];
      }
      
      else if (outTree->n_bjetsLoose == 2) {
          outTree->bjet2Pt   = tempJet->Pt();
          outTree->bjet2Eta  = tempJet->Eta();
          outTree->bjet2Phi  = tempJet->Phi();
          outTree->bjet2M    = tempJet->M();
          outTree->bjet2BTag = (*(inTree->jetBdiscr))[iJet];
      }
    }
    
    //// Now check number of non-overlapping taus ////

    for (Int_t iTau = 0; iTau < inTree->tauP4->GetEntries(); iTau++) {
      TLorentzVector* tempTau = (TLorentzVector*) inTree->tauP4->At(iTau);

      if (tempTau->Pt() < 18. || fabs(tempTau->Eta()) > 2.3)
        continue;

      if (((*(inTree->tauSelBits))[iTau] & 7) != 7) 
        continue;
      if ((*(inTree->tauIsoDeltaBetaCorr))[iTau] > 4.5)
        continue;

      //// Now do cleaning ////
      
      Bool_t match = false;
      
      for (UInt_t iLepton = 0; iLepton < leptonVecs.size(); iLepton++) {
        if (deltaR(leptonVecs[iLepton]->Phi(),leptonVecs[iLepton]->Eta(),tempTau->Phi(),tempTau->Eta()) < dROverlap) {
          match = true;
          break;
        }
      }
      
      if (match)
        continue;

      float dR_1 = dROverlap + 0.1;
      float dR_2 = dROverlap + 0.1;

      if (outTree->lep1Pt > 0)
        dR_1 = deltaR(outTree->lep1Phi, outTree->lep1Eta, tempTau->Phi(),tempTau->Eta());
      if (outTree->lep2Pt > 0)
        dR_2 = deltaR(outTree->lep2Phi, outTree->lep2Eta, tempTau->Phi(),tempTau->Eta());

      if (dR_1 > dROverlap && dR_2 > dROverlap)
        outTree->n_tau++;
    }
    
    //// Fat Jet Selection ////

    for (Int_t iFatJet = 0; iFatJet < inTree->fatjetak8P4->GetEntries(); iFatJet++) {
      TLorentzVector* tempFatJet = (TLorentzVector*) inTree->fatjetak8P4->At(iFatJet);

      // Clean the fat jets

      Bool_t match = false;

      for (UInt_t iLepton = 0; iLepton < leptonVecs.size(); iLepton++) {
        if (deltaR(leptonVecs[iLepton]->Phi(),leptonVecs[iLepton]->Eta(),tempFatJet->Phi(),tempFatJet->Eta()) < 2.0 * dROverlap) {
          match = true;
          break;
        }
      }
      
      for (UInt_t iPhoton = 0; iPhoton < photonVecs.size(); iPhoton++) {
        if (deltaR(photonVecs[iPhoton]->Phi(),photonVecs[iPhoton]->Eta(),tempFatJet->Phi(),tempFatJet->Eta()) < 2.0 * dROverlap) {
          match = true;
          break;
        }
      }

      if (match)
        continue;

//       float top1 = vectorSumMass(tempFatJet->Pt(), tempFatJet->Eta(), tempFatJet->Phi(), (*(inTree->fatjetak8PrunedMass))[iFatJet], 
//                                  outTree->bjet1Pt, outTree->bjet1Eta, outTree->bjet1Phi, outTree->bjet1M);
//       float top2 = vectorSumMass(tempFatJet->Pt(), tempFatJet->Eta(), tempFatJet->Phi(), (*(inTree->fatjetak8PrunedMass))[iFatJet], 
//                                  outTree->bjet2Pt, outTree->bjet2Eta, outTree->bjet2Phi, outTree->bjet2M);
      
//       if ((top1 > 250) && (top2 > 250))
//         continue;

      if (outTree->fatjet1Pt < 0) {
        outTree->fatjet1Pt   = tempFatJet->Pt();
        outTree->fatjet1Eta  = tempFatJet->Eta();
        outTree->fatjet1Phi  = tempFatJet->Phi();
        outTree->fatjet1Mass = tempFatJet->M();
        outTree->fatjet1TrimmedM  = (*(inTree->fatjetak8TrimmedMass))[iFatJet];
        outTree->fatjet1PrunedM   = (*(inTree->fatjetak8PrunedMass))[iFatJet];
        outTree->fatjet1FilteredM = (*(inTree->fatjetak8FilteredMass))[iFatJet];
        outTree->fatjet1SoftDropM = (*(inTree->fatjetak8SoftdropMass))[iFatJet];
        outTree->fatjet1tau1  = (*(inTree->fatjetak8Tau1))[iFatJet];
        outTree->fatjet1tau2  = (*(inTree->fatjetak8Tau2))[iFatJet];
        outTree->fatjet1tau21 = outTree->fatjet1tau2/outTree->fatjet1tau1;

        for (Int_t iJet = 0; iJet < inTree->jetP4->GetEntries(); iJet++) {
          TLorentzVector* tempJet = (TLorentzVector*) inTree->jetP4->At(iJet);
          checkDR = deltaR(outTree->fatjet1Phi,outTree->fatjet1Eta,tempJet->Phi(),tempJet->Eta());

          // Check loose distance
          if ((*(inTree->jetBdiscr))[iJet] > bCutLoose) {
            if (checkDR < outTree->fatjet1DRLooseB)
                outTree->fatjet1DRLooseB = checkDR;

            // Check medium distance
            if ((*(inTree->jetBdiscr))[iJet] > bCutMedium) {
              if (checkDR < outTree->fatjet1DRMediumB)
                outTree->fatjet1DRMediumB = checkDR;

              // Check tight distance
              if ((*(inTree->jetBdiscr))[iJet] > bCutTight) {
                if (checkDR < outTree->fatjet1DRTightB)
                  outTree->fatjet1DRTightB = checkDR;
              }
            }
          }
        }

        if (outTree->lep1Pt > 0)
          outTree->fatjet1DPhiLep1 = deltaPhi(outTree->fatjet1Phi, outTree->lep1Phi);

        if (inTree->metP4_GEN->GetEntries() > 0) {
          for (Int_t iGen = 0; iGen < inTree->genP4->GetEntries(); iGen++) {
            Int_t checkPdgId = abs((*(inTree->genPdgId))[iGen]);
            if (checkPdgId != 23 && checkPdgId != 24)
              continue;

            TLorentzVector *tempGen = (TLorentzVector*) inTree->genP4->At(iGen);
            checkDR = deltaR(outTree->fatjet1Phi,outTree->fatjet1Eta,tempGen->Phi(),tempGen->Eta());
            if (checkDR < outTree->fatjet1DRGenW) {
              outTree->fatjet1DRGenW   = checkDR;
              outTree->fatjet1GenWPt   = tempGen->Pt();
              outTree->fatjet1GenWMass = tempGen->M();
            }
          }
        }
      }

      else if (outTree->fatjet2Pt < 0) {
        outTree->fatjet2Pt   = tempFatJet->Pt();
        outTree->fatjet2Eta  = tempFatJet->Eta();
        outTree->fatjet2Phi  = tempFatJet->Phi();
        outTree->fatjet2Mass = tempFatJet->M();
        outTree->fatjet2TrimmedM  = (*(inTree->fatjetak8TrimmedMass))[iFatJet];
        outTree->fatjet2PrunedM   = (*(inTree->fatjetak8PrunedMass))[iFatJet];
        outTree->fatjet2FilteredM = (*(inTree->fatjetak8FilteredMass))[iFatJet];
        outTree->fatjet2SoftDropM = (*(inTree->fatjetak8SoftdropMass))[iFatJet];
        outTree->fatjet2tau1  = (*(inTree->fatjetak8Tau1))[iFatJet];
        outTree->fatjet2tau2  = (*(inTree->fatjetak8Tau2))[iFatJet];
        outTree->fatjet2tau21 = outTree->fatjet2tau2/outTree->fatjet2tau1;

        for (Int_t iJet = 0; iJet < inTree->jetP4->GetEntries(); iJet++) {
          TLorentzVector* tempJet = (TLorentzVector*) inTree->jetP4->At(iJet);
          checkDR = deltaR(outTree->fatjet2Phi,outTree->fatjet2Eta,tempJet->Phi(),tempJet->Eta());

          // Check loose distance
          if ((*(inTree->jetBdiscr))[iJet] > bCutLoose) {
            if (checkDR < outTree->fatjet2DRLooseB)
                outTree->fatjet2DRLooseB = checkDR;

            // Check medium distance
            if ((*(inTree->jetBdiscr))[iJet] > bCutMedium) {
              if (checkDR < outTree->fatjet2DRMediumB)
                outTree->fatjet2DRMediumB = checkDR;

              // Check tight distance
              if ((*(inTree->jetBdiscr))[iJet] > bCutTight) {
                if (checkDR < outTree->fatjet2DRTightB)
                  outTree->fatjet2DRTightB = checkDR;
              }
            }
          }
        }

        if (outTree->lep1Pt > 0)
          outTree->fatjet2DPhiLep1 = deltaPhi(outTree->fatjet2Phi, outTree->lep1Phi);

        if (inTree->metP4_GEN->GetEntries() > 0) {
          for (Int_t iGen = 0; iGen < inTree->genP4->GetEntries(); iGen++) {
            Int_t checkPdgId = abs((*(inTree->genPdgId))[iGen]);
            if (checkPdgId != 23 && checkPdgId != 24)
              continue;

            TLorentzVector *tempGen = (TLorentzVector*) inTree->genP4->At(iGen);
            checkDR = deltaR(outTree->fatjet2Phi,outTree->fatjet2Eta,tempGen->Phi(),tempGen->Eta());
            if (checkDR < outTree->fatjet2DRGenW) {
              outTree->fatjet2DRGenW   = checkDR;
              outTree->fatjet2GenWPt   = tempGen->Pt();
              outTree->fatjet2GenWMass = tempGen->M();
            }
          }
        }
      }
    }

    float pt1 = -0.5;
    float pt2 = -0.5;

    if (inTree->metP4_GEN->GetEntries() > 0) {
      for (Int_t iGen = 0; iGen < inTree->genP4->GetEntries(); iGen++) {
        Int_t checkPdgId = abs((*(inTree->genPdgId))[iGen]);
        if (abs(checkPdgId) == 6){
          if (checkPdgId > 0.0)
            pt1 = ((TLorentzVector*) inTree->genP4->At(iGen))->Pt();
          else
            pt2 = ((TLorentzVector*) inTree->genP4->At(iGen))->Pt();
        }
      }
      if (pt1 > 0.0 && pt2 > 0.0)
        outTree->topPtReweighting = 1.001 * sqrt(exp(0.156 - 0.00137*min(pt1,float(400.0))) * 
                                                 exp(0.156 - 0.00137*min(pt2,float(400.0))));
    }

    if (outTree->bjet2Pt > 0) {
      if (outTree->fatjet1Pt > 0) {
        outTree->topMass_11 = vectorSumMass(outTree->fatjet1Pt,outTree->fatjet1Eta,outTree->fatjet1Phi,outTree->fatjet1Mass,
                                            outTree->bjet1Pt,outTree->bjet1Eta,outTree->bjet1Phi,outTree->bjet1M);
        outTree->topMass_12 = vectorSumMass(outTree->fatjet1Pt,outTree->fatjet1Eta,outTree->fatjet1Phi,outTree->fatjet1Mass,
                                            outTree->bjet2Pt,outTree->bjet2Eta,outTree->bjet2Phi,outTree->bjet2M);
        outTree->topPrunedM_11 = vectorSumMass(outTree->fatjet1Pt,outTree->fatjet1Eta,outTree->fatjet1Phi,outTree->fatjet1PrunedM,
                                               outTree->bjet1Pt,outTree->bjet1Eta,outTree->bjet1Phi,outTree->bjet1M);
        outTree->topPrunedM_12 = vectorSumMass(outTree->fatjet1Pt,outTree->fatjet1Eta,outTree->fatjet1Phi,outTree->fatjet1PrunedM,
                                               outTree->bjet2Pt,outTree->bjet2Eta,outTree->bjet2Phi,outTree->bjet2M);
      }
      if (outTree->fatjet2Pt > 0) {
        outTree->topMass_21 = vectorSumMass(outTree->fatjet2Pt,outTree->fatjet2Eta,outTree->fatjet2Phi,outTree->fatjet2Mass,
                                            outTree->bjet1Pt,outTree->bjet1Eta,outTree->bjet1Phi,outTree->bjet1M);
        outTree->topMass_22 = vectorSumMass(outTree->fatjet2Pt,outTree->fatjet2Eta,outTree->fatjet2Phi,outTree->fatjet2Mass,
                                            outTree->bjet2Pt,outTree->bjet2Eta,outTree->bjet2Phi,outTree->bjet2M);
        outTree->topPrunedM_21 = vectorSumMass(outTree->fatjet2Pt,outTree->fatjet2Eta,outTree->fatjet2Phi,outTree->fatjet2PrunedM,
                                               outTree->bjet1Pt,outTree->bjet1Eta,outTree->bjet1Phi,outTree->bjet1M);
        outTree->topPrunedM_22 = vectorSumMass(outTree->fatjet2Pt,outTree->fatjet2Eta,outTree->fatjet2Phi,outTree->fatjet2PrunedM,
                                               outTree->bjet2Pt,outTree->bjet2Eta,outTree->bjet2Phi,outTree->bjet2M);
      }
    }

    outTree->Fill();

  }

  outTree->WriteToFile(outFile);
  outFile->Close();
  inFile->Close();
}
