#include "Nero_30fb.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void Nero_30fb::Loop()
{
//   In a ROOT session, you can do:
//      root> .L Nero_30fb.C
//      root> Nero_30fb t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
   }
}

Nero_30fb::Nero_30fb(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/afs/cern.ch/work/d/dabercro/eoscms/cms/store/group/phys_higgs/ceballos/setup80x_ichep/Data/Nero/v2.0/SingleMuon/SingleMuon-Run2016E-23Sep2016/161208_212714/0000/NeroNtuples_10.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/afs/cern.ch/work/d/dabercro/eoscms/cms/store/group/phys_higgs/ceballos/setup80x_ichep/Data/Nero/v2.0/SingleMuon/SingleMuon-Run2016E-23Sep2016/161208_212714/0000/NeroNtuples_10.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("/afs/cern.ch/work/d/dabercro/eoscms/cms/store/group/phys_higgs/ceballos/setup80x_ichep/Data/Nero/v2.0/SingleMuon/SingleMuon-Run2016E-23Sep2016/161208_212714/0000/NeroNtuples_10.root:/nero");
      dir->GetObject("events",tree);

   }
   Init(tree);
}

Nero_30fb::~Nero_30fb()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t Nero_30fb::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t Nero_30fb::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void Nero_30fb::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   jetP4 = 0;
   jetMatch = 0;
   jetRawPt = 0;
   jetRefPt = 0;
   jetBdiscr = 0;
   jetPuId = 0;
   jetUnc = 0;
   jetchef = 0;
   jetnhef = 0;
   jetnemf = 0;
   jetcemf = 0;
   jetQGL = 0;
   jetQglMult = 0;
   jetQglPtD = 0;
   jetQglAxis2 = 0;
   jetFlavour = 0;
   jetMatchedPartonPdgId = 0;
   jetMotherPdgId = 0;
   jetGrMotherPdgId = 0;
   jetSelBits = 0;
   jetQ = 0;
   jetPtResUncCentral = 0;
   jetPtResUncUp = 0;
   jetPtResUncDown = 0;
   jetpuppiP4 = 0;
   jetpuppiRawPt = 0;
   jetpuppiBdiscr = 0;
   jetpuppiSelBits = 0;
   jetpuppiQ = 0;
   fatjetAK8CHSP4 = 0;
   fatjetAK8CHSRawPt = 0;
   fatjetAK8CHSFlavour = 0;
   fatjetAK8CHSTau1 = 0;
   fatjetAK8CHSTau2 = 0;
   fatjetAK8CHSTau3 = 0;
   fatjetAK8CHSTrimmedMass = 0;
   fatjetAK8CHSPrunedMass = 0;
   fatjetAK8CHSCorrectedPrunedMass = 0;
   fatjetAK8CHSSoftdropMass = 0;
   fatjetAK8CHSsubjet = 0;
   fatjetAK8CHSnSubjets = 0;
   fatjetAK8CHSfirstSubjet = 0;
   fatjetAK8CHSsubjet_btag = 0;
   fatjetAK8CHSHbb = 0;
   fatjetAK8CHStopMVA = 0;
   puppiAK8 = 0;
   puppi_tau1 = 0;
   puppi_tau2 = 0;
   puppi_softdrop_masscorr = 0;
   puppi_softdrop_mass = 0;
   tauP4 = 0;
   tauMatch = 0;
   tauSelBits = 0;
   tauQ = 0;
   tauM = 0;
   tauIso = 0;
   tauLeadTrackPt = 0;
   tauChargedIsoPtSum = 0;
   tauNeutralIsoPtSum = 0;
   tauIsoDeltaBetaCorr = 0;
   tauIsoPileupWeightedRaw = 0;
   tauIsoMva = 0;
   lepP4 = 0;
   lepMatch = 0;
   lepPdgId = 0;
   lepIso = 0;
   lepSelBits = 0;
   lepPfPt = 0;
   lepMva = 0;
   lepChIso = 0;
   lepNhIso = 0;
   lepPhoIso = 0;
   lepPuIso = 0;
   lepMiniIso = 0;
   lepEtaSC = 0;
   lepSieie = 0;
   lepSipip = 0;
   lepSieip = 0;
   lepR9 = 0;
   eleP4_smear = 0;
   metP4 = 0;
   metP4_GEN = 0;
   metPuppi = 0;
   metPuppiSyst = 0;
   metSyst = 0;
   CaloMet = 0;
   RawMet = 0;
   metNoMu = 0;
   pfMet_e3p0 = 0;
   trackMet = 0;
   neutralMet = 0;
   photonMet = 0;
   HFMet = 0;
   SmearedMet = 0;
   photonP4 = 0;
   photonIso = 0;
   photonSieie = 0;
   photonSelBits = 0;
   photonChIso = 0;
   photonNhIso = 0;
   photonPhoIso = 0;
   photonPuIso = 0;
   phoP4_smear = 0;
   photonRawPt = 0;
   photonRawScEnergy = 0;
   photonHOverE = 0;
   photonChWorstIso = 0;
   photonChIsoMax = 0;
   photonEmax = 0;
   photonE2nd = 0;
   photonE33 = 0;
   photonE55 = 0;
   photonSipip = 0;
   photonSieip = 0;
   photonR9 = 0;
   photonEtaSC = 0;
   photonS4 = 0;
   photonMipEnergy = 0;
   photonTime = 0;
   photonTimeSpan = 0;
   photonGenMatched = 0;
   genP4 = 0;
   genjetP4 = 0;
   genPdgId = 0;
   genFlags = 0;
   genIso = 0;
   genParent = 0;
   triggerFired = 0;
   triggerPrescale = 0;
   triggerLeps = 0;
   triggerJets = 0;
   triggerTaus = 0;
   triggerPhotons = 0;
   triggerNoneTaus = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("isRealData", &isRealData, &b_isRealData);
   fChain->SetBranchAddress("runNum", &runNum, &b_runNum);
   fChain->SetBranchAddress("lumiNum", &lumiNum, &b_lumiNum);
   fChain->SetBranchAddress("eventNum", &eventNum, &b_eventNum);
   fChain->SetBranchAddress("rho", &rho, &b_rho);
   fChain->SetBranchAddress("filterSelBits", &filterSelBits, &b_selBits);
   fChain->SetBranchAddress("filterbadChCandidate", &filterbadChCandidate, &b_filterbadChCandidate);
   fChain->SetBranchAddress("filterbadPFMuon", &filterbadPFMuon, &b_filterbadPFMuon);
   fChain->SetBranchAddress("npv", &npv, &b_npv);
   fChain->SetBranchAddress("jetP4", &jetP4, &b_jetP4);
   fChain->SetBranchAddress("jetMatch", &jetMatch, &b_jetMatch);
   fChain->SetBranchAddress("jetRawPt", &jetRawPt, &b_jetRawPt);
   fChain->SetBranchAddress("jetRefPt", &jetRefPt, &b_jetRefPt);
   fChain->SetBranchAddress("jetBdiscr", &jetBdiscr, &b_jetBdiscr);
   fChain->SetBranchAddress("jetPuId", &jetPuId, &b_jetPuId);
   fChain->SetBranchAddress("jetUnc", &jetUnc, &b_jetUnc);
   fChain->SetBranchAddress("jetchef", &jetchef, &b_jetchef);
   fChain->SetBranchAddress("jetnhef", &jetnhef, &b_jetnhef);
   fChain->SetBranchAddress("jetnemf", &jetnemf, &b_jetnemf);
   fChain->SetBranchAddress("jetcemf", &jetcemf, &b_jetcemf);
   fChain->SetBranchAddress("jetQGL", &jetQGL, &b_jetQGL);
   fChain->SetBranchAddress("jetQglMult", &jetQglMult, &b_jetQglMult);
   fChain->SetBranchAddress("jetQglPtD", &jetQglPtD, &b_jetQglPtD);
   fChain->SetBranchAddress("jetQglAxis2", &jetQglAxis2, &b_jetQglAxis2);
   fChain->SetBranchAddress("jetFlavour", &jetFlavour, &b_jetFlavour);
   fChain->SetBranchAddress("jetMatchedPartonPdgId", &jetMatchedPartonPdgId, &b_jetMatchedPartonPdgId);
   fChain->SetBranchAddress("jetMotherPdgId", &jetMotherPdgId, &b_jetMotherPdgId);
   fChain->SetBranchAddress("jetGrMotherPdgId", &jetGrMotherPdgId, &b_jetGrMotherPdgId);
   fChain->SetBranchAddress("jetSelBits", &jetSelBits, &b_jetSelBits);
   fChain->SetBranchAddress("jetQ", &jetQ, &b_jetQ);
   fChain->SetBranchAddress("jetPtResUncCentral", &jetPtResUncCentral, &b_jetPtResUncCentral);
   fChain->SetBranchAddress("jetPtResUncUp", &jetPtResUncUp, &b_jetPtResUncUp);
   fChain->SetBranchAddress("jetPtResUncDown", &jetPtResUncDown, &b_jetPtResUncDown);
   fChain->SetBranchAddress("jetpuppiP4", &jetpuppiP4, &b_jetpuppiP4);
   fChain->SetBranchAddress("jetpuppiRawPt", &jetpuppiRawPt, &b_jetpuppiRawPt);
   fChain->SetBranchAddress("jetpuppiBdiscr", &jetpuppiBdiscr, &b_jetpuppiBdiscr);
   fChain->SetBranchAddress("jetpuppiSelBits", &jetpuppiSelBits, &b_jetpuppiSelBits);
   fChain->SetBranchAddress("jetpuppiQ", &jetpuppiQ, &b_jetpuppiQ);
   fChain->SetBranchAddress("fatjetAK8CHSP4", &fatjetAK8CHSP4, &b_fatjetAK8CHSP4);
   fChain->SetBranchAddress("fatjetAK8CHSRawPt", &fatjetAK8CHSRawPt, &b_fatjetAK8CHSRawPt);
   fChain->SetBranchAddress("fatjetAK8CHSFlavour", &fatjetAK8CHSFlavour, &b_fatjetAK8CHSFlavour);
   fChain->SetBranchAddress("fatjetAK8CHSTau1", &fatjetAK8CHSTau1, &b_fatjetAK8CHSTau1);
   fChain->SetBranchAddress("fatjetAK8CHSTau2", &fatjetAK8CHSTau2, &b_fatjetAK8CHSTau2);
   fChain->SetBranchAddress("fatjetAK8CHSTau3", &fatjetAK8CHSTau3, &b_fatjetAK8CHSTau3);
   fChain->SetBranchAddress("fatjetAK8CHSTrimmedMass", &fatjetAK8CHSTrimmedMass, &b_fatjetAK8CHSTrimmedMass);
   fChain->SetBranchAddress("fatjetAK8CHSPrunedMass", &fatjetAK8CHSPrunedMass, &b_fatjetAK8CHSPrunedMass);
   fChain->SetBranchAddress("fatjetAK8CHSCorrectedPrunedMass", &fatjetAK8CHSCorrectedPrunedMass, &b_fatjetAK8CHSCorrectedPrunedMass);
   fChain->SetBranchAddress("fatjetAK8CHSSoftdropMass", &fatjetAK8CHSSoftdropMass, &b_fatjetAK8CHSSoftdropMass);
   fChain->SetBranchAddress("fatjetAK8CHSsubjet", &fatjetAK8CHSsubjet, &b_fatjetAK8CHSsubjet);
   fChain->SetBranchAddress("fatjetAK8CHSnSubjets", &fatjetAK8CHSnSubjets, &b_fatjetAK8CHSnSubjets);
   fChain->SetBranchAddress("fatjetAK8CHSfirstSubjet", &fatjetAK8CHSfirstSubjet, &b_fatjetAK8CHSfirstSubjet);
   fChain->SetBranchAddress("fatjetAK8CHSsubjet_btag", &fatjetAK8CHSsubjet_btag, &b_fatjetAK8CHSsubjet_btag);
   fChain->SetBranchAddress("fatjetAK8CHSHbb", &fatjetAK8CHSHbb, &b_fatjetAK8CHSHbb);
   fChain->SetBranchAddress("fatjetAK8CHStopMVA", &fatjetAK8CHStopMVA, &b_fatjetAK8CHStopMVA);
   fChain->SetBranchAddress("puppiAK8", &puppiAK8, &b_puppiAK8);
   fChain->SetBranchAddress("puppi_tau1", &puppi_tau1, &b_puppi_tau1);
   fChain->SetBranchAddress("puppi_tau2", &puppi_tau2, &b_puppi_tau2);
   fChain->SetBranchAddress("puppi_softdrop_masscorr", &puppi_softdrop_masscorr, &b_puppi_softdrop_masscorr);
   fChain->SetBranchAddress("puppi_softdrop_mass", &puppi_softdrop_mass, &b_puppi_softdrop_mass);
   fChain->SetBranchAddress("tauP4", &tauP4, &b_tauP4);
   fChain->SetBranchAddress("tauMatch", &tauMatch, &b_tauMatch);
   fChain->SetBranchAddress("tauSelBits", &tauSelBits, &b_tauSelBits);
   fChain->SetBranchAddress("tauQ", &tauQ, &b_tauQ);
   fChain->SetBranchAddress("tauM", &tauM, &b_tauM);
   fChain->SetBranchAddress("tauIso", &tauIso, &b_tauIso);
   fChain->SetBranchAddress("tauLeadTrackPt", &tauLeadTrackPt, &b_tauLeadTrackPt);
   fChain->SetBranchAddress("tauChargedIsoPtSum", &tauChargedIsoPtSum, &b_tauChargedIsoPtSum);
   fChain->SetBranchAddress("tauNeutralIsoPtSum", &tauNeutralIsoPtSum, &b_tauNeutralIsoPtSum);
   fChain->SetBranchAddress("tauIsoDeltaBetaCorr", &tauIsoDeltaBetaCorr, &b_tauIsoDeltaBetaCorr);
   fChain->SetBranchAddress("tauIsoPileupWeightedRaw", &tauIsoPileupWeightedRaw, &b_tauIsoPileupWeightedRaw);
   fChain->SetBranchAddress("tauIsoMva", &tauIsoMva, &b_tauIsoMva);
   fChain->SetBranchAddress("lepP4", &lepP4, &b_lepP4);
   fChain->SetBranchAddress("lepMatch", &lepMatch, &b_lepMatch);
   fChain->SetBranchAddress("lepPdgId", &lepPdgId, &b_lepPdgId);
   fChain->SetBranchAddress("lepIso", &lepIso, &b_lepIso);
   fChain->SetBranchAddress("lepSelBits", &lepSelBits, &b_lepSelBits);
   fChain->SetBranchAddress("lepPfPt", &lepPfPt, &b_lepPfPt);
   fChain->SetBranchAddress("lepMva", &lepMva, &b_lepMva);
   fChain->SetBranchAddress("lepChIso", &lepChIso, &b_lepChIso);
   fChain->SetBranchAddress("lepNhIso", &lepNhIso, &b_lepNhIso);
   fChain->SetBranchAddress("lepPhoIso", &lepPhoIso, &b_lepPhoIso);
   fChain->SetBranchAddress("lepPuIso", &lepPuIso, &b_lepPuIso);
   fChain->SetBranchAddress("lepMiniIso", &lepMiniIso, &b_lepMiniIso);
   fChain->SetBranchAddress("lepEtaSC", &lepEtaSC, &b_lepEtaSC);
   fChain->SetBranchAddress("lepSieie", &lepSieie, &b_lepSieie);
   fChain->SetBranchAddress("lepSipip", &lepSipip, &b_lepSipip);
   fChain->SetBranchAddress("lepSieip", &lepSieip, &b_lepSieip);
   fChain->SetBranchAddress("lepR9", &lepR9, &b_lepR9);
   fChain->SetBranchAddress("eleP4_smear", &eleP4_smear, &b_eleP4_smear);
   fChain->SetBranchAddress("metP4", &metP4, &b_metP4);
   fChain->SetBranchAddress("metP4_GEN", &metP4_GEN, &b_metP4_GEN);
   fChain->SetBranchAddress("metPuppi", &metPuppi, &b_metPuppi);
   fChain->SetBranchAddress("metPuppiSyst", &metPuppiSyst, &b_metPuppiSyst);
   fChain->SetBranchAddress("metSyst", &metSyst, &b_metSyst);
   fChain->SetBranchAddress("CaloMet", &CaloMet, &b_CaloMet);
   fChain->SetBranchAddress("RawMet", &RawMet, &b_RawMet);
   fChain->SetBranchAddress("metNoMu", &metNoMu, &b_metNoMu);
   fChain->SetBranchAddress("pfMet_e3p0", &pfMet_e3p0, &b_pfMet_e3p0);
   fChain->SetBranchAddress("trackMet", &trackMet, &b_trackMet);
   fChain->SetBranchAddress("neutralMet", &neutralMet, &b_neutralMet);
   fChain->SetBranchAddress("photonMet", &photonMet, &b_photonMet);
   fChain->SetBranchAddress("HFMet", &HFMet, &b_HFMet);
   fChain->SetBranchAddress("SmearedMet", &SmearedMet, &b_SmearedMet);
   fChain->SetBranchAddress("photonP4", &photonP4, &b_photonP4);
   fChain->SetBranchAddress("photonIso", &photonIso, &b_photonIso);
   fChain->SetBranchAddress("photonSieie", &photonSieie, &b_photonSieie);
   fChain->SetBranchAddress("photonSelBits", &photonSelBits, &b_photonSelBits);
   fChain->SetBranchAddress("photonChIso", &photonChIso, &b_photonChIso);
   fChain->SetBranchAddress("photonNhIso", &photonNhIso, &b_photonNhIso);
   fChain->SetBranchAddress("photonPhoIso", &photonPhoIso, &b_photonPhoIso);
   fChain->SetBranchAddress("photonPuIso", &photonPuIso, &b_photonPuIso);
   fChain->SetBranchAddress("phoP4_smear", &phoP4_smear, &b_phoP4_smear);
   fChain->SetBranchAddress("photonRawPt", &photonRawPt, &b_photonRawPt);
   fChain->SetBranchAddress("photonRawScEnergy", &photonRawScEnergy, &b_photonRawScEnergy);
   fChain->SetBranchAddress("photonHOverE", &photonHOverE, &b_photonHOverE);
   fChain->SetBranchAddress("photonChWorstIso", &photonChWorstIso, &b_photonChWorstIso);
   fChain->SetBranchAddress("photonChIsoMax", &photonChIsoMax, &b_photonChIsoMax);
   fChain->SetBranchAddress("photonEmax", &photonEmax, &b_photonEmax);
   fChain->SetBranchAddress("photonE2nd", &photonE2nd, &b_photonE2nd);
   fChain->SetBranchAddress("photonE33", &photonE33, &b_photonE33);
   fChain->SetBranchAddress("photonE55", &photonE55, &b_photonE55);
   fChain->SetBranchAddress("photonSipip", &photonSipip, &b_photonSipip);
   fChain->SetBranchAddress("photonSieip", &photonSieip, &b_photonSieip);
   fChain->SetBranchAddress("photonR9", &photonR9, &b_photonR9);
   fChain->SetBranchAddress("photonEtaSC", &photonEtaSC, &b_photonEtaSC);
   fChain->SetBranchAddress("photonS4", &photonS4, &b_photonS4);
   fChain->SetBranchAddress("photonMipEnergy", &photonMipEnergy, &b_photonMipEnergy);
   fChain->SetBranchAddress("photonTime", &photonTime, &b_photonTime);
   fChain->SetBranchAddress("photonTimeSpan", &photonTimeSpan, &b_photonTimeSpan);
   fChain->SetBranchAddress("photonGenMatched", &photonGenMatched, &b_photonGenMatched);
   fChain->SetBranchAddress("genP4", &genP4, &b_genP4);
   fChain->SetBranchAddress("genjetP4", &genjetP4, &b_genjetP4);
   fChain->SetBranchAddress("genPdgId", &genPdgId, &b_genPdgId);
   fChain->SetBranchAddress("genFlags", &genFlags, &b_genFlags);
   fChain->SetBranchAddress("puTrueInt", &puTrueInt, &b_puTrueInt);
   fChain->SetBranchAddress("mcWeight", &mcWeight, &b_mcWeight);
   fChain->SetBranchAddress("r2f1", &r2f1, &b_r2f1);
   fChain->SetBranchAddress("r5f1", &r5f1, &b_r5f1);
   fChain->SetBranchAddress("r1f2", &r1f2, &b_r1f2);
   fChain->SetBranchAddress("r2f2", &r2f2, &b_r2f2);
   fChain->SetBranchAddress("r1f5", &r1f5, &b_r1f5);
   fChain->SetBranchAddress("r5f5", &r5f5, &b_r5f5);
   fChain->SetBranchAddress("genIso", &genIso, &b_genIso);
   fChain->SetBranchAddress("genParent", &genParent, &b_genParent);
   fChain->SetBranchAddress("triggerFired", &triggerFired, &b_triggerFired);
   fChain->SetBranchAddress("triggerPrescale", &triggerPrescale, &b_triggerPrescale);
   fChain->SetBranchAddress("triggerLeps", &triggerLeps, &b_triggerLeps);
   fChain->SetBranchAddress("triggerJets", &triggerJets, &b_triggerJets);
   fChain->SetBranchAddress("triggerTaus", &triggerTaus, &b_triggerTaus);
   fChain->SetBranchAddress("triggerPhotons", &triggerPhotons, &b_triggerPhotons);
   fChain->SetBranchAddress("triggerNoneTaus", &triggerNoneTaus, &b_triggerNoneTaus);
   Notify();
}

Bool_t Nero_30fb::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void Nero_30fb::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t Nero_30fb::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
