// For smearing the Pruned Mass of jets

#ifndef JETSMEARER_H
#define JETSMEARER_H

#include <vector>
#include <iostream>
#include <fstream>

#include "TF1.h"
#include "TMath.h"
#include "TRandom2.h"

#include "NeroTree.h"
#include "KinematicFunctions.h"

enum SmearType { kCentral = 0, kUp, kDown };

class JetSmearer {
 public:
  JetSmearer (NeroTree* thisTree) { fNeroTree = thisTree; }
  virtual ~JetSmearer() {}

  void ReadSFConfig   ( TString configName );
  void ReadResConfig  ( TString configName );

  Float_t GetSmeared  ( Float_t rho, Float_t jetPt, Float_t jetEta, Float_t jetPhi, Float_t toSmear, SmearType smearing );

 private:

  NeroTree *fNeroTree;

  std::vector<Float_t> SFDownEta;
  std::vector<Float_t> SFUpEta;
  std::vector<Float_t> SFs;
  std::vector<Float_t> DownSFs;
  std::vector<Float_t> UpSFs;

  std::vector<Float_t> ResDownEta;
  std::vector<Float_t> ResUpEta;
  std::vector<Float_t> ResDownRho;
  std::vector<Float_t> ResUpRho;

  std::vector<Double_t> ResParam0;
  std::vector<Double_t> ResParam1;
  std::vector<Double_t> ResParam2;
  std::vector<Double_t> ResParam3;

  TF1 ResFormula = TF1("ResFormula","sqrt([0]*abs([0])/(x*x)+[1]*[1]*pow(x,[3])+[2]*[2])",0,5000);
  TRandom2 generator = TRandom2();
};

void JetSmearer::ReadSFConfig(TString configName)
{
  std::ifstream configFile;
  configFile.open(configName.Data());
  Float_t downEta = 0.0;
  Float_t upEta = 0.0;
  Float_t sf = 1.0;
  Float_t downSf = 1.0;
  Float_t upSf = 1.0;

  TString Stuff = "";

  while(!Stuff.EndsWith("}"))
    configFile >> Stuff;
  
  while(!configFile.eof()) {
    configFile >> downEta >> upEta >> Stuff >> sf >> downSf >> upSf;
    SFDownEta.push_back(downEta);
    SFUpEta.push_back(upEta);
    SFs.push_back(sf);
    DownSFs.push_back(downSf);
    UpSFs.push_back(upSf);
    
  }
  configFile.close();
}

void JetSmearer::ReadResConfig(TString configName)
{
  std::ifstream configFile;
  configFile.open(configName.Data());
  Float_t downEta = 0.0;
  Float_t upEta = 0.0;
  Float_t downRho = 0.0;
  Float_t upRho = 0.0;

  Double_t param0 = 0.0;
  Double_t param1 = 0.0;
  Double_t param2 = 0.0;
  Double_t param3 = 0.0;

  TString Stuff = "";

  while(!Stuff.EndsWith("}"))
    configFile >> Stuff;
  
  while(!configFile.eof()) {
    configFile >> downEta >> upEta >> downRho >> upRho;
    configFile >> Stuff;
    configFile >> Stuff;
    configFile >> Stuff;
    
    configFile >> param0 >> param1 >> param2 >> param3;

    ResDownEta.push_back(downEta);
    ResUpEta.push_back(upEta);
    ResDownRho.push_back(downRho);
    ResUpRho.push_back(upRho);
    ResParam0.push_back(param0);
    ResParam1.push_back(param1);
    ResParam2.push_back(param2);
    ResParam3.push_back(param3);
  }
  configFile.close();
}

Float_t JetSmearer::GetSmeared(Float_t rho, Float_t jetPt, Float_t jetEta, Float_t jetPhi,
                               Float_t toSmear, SmearType smearing)
{
  UInt_t SFIndex = 0;
  UInt_t ResIndex = 0;

  Bool_t pleaseScale = false;
  Float_t genPt = 0.0;

  for (UInt_t iSF = 0; iSF != SFDownEta.size(); ++iSF) {
    if (jetEta < SFUpEta[iSF]) {
      SFIndex = iSF;
      break;
    }
  }

  for (UInt_t iRes = 0; iRes != ResDownEta.size(); ++iRes) {
    if (jetEta < ResUpEta[iRes] && rho < ResUpRho[iRes]) {
      ResIndex = iRes;
      break;
    }
  }

  ResFormula.SetParameter(0,ResParam0[ResIndex]);
  ResFormula.SetParameter(1,ResParam1[ResIndex]);
  ResFormula.SetParameter(2,ResParam2[ResIndex]);
  ResFormula.SetParameter(3,ResParam3[ResIndex]);

  Float_t res = ResFormula.Eval(jetPt);
  Float_t sf = 1.0;
  if (smearing == kCentral)
    sf = SFs[SFIndex];
  else if (smearing == kUp)
    sf = UpSFs[SFIndex];
  else if (smearing == kDown)
    sf = DownSFs[SFIndex];
  else
    return toSmear;

  for (Int_t iGenJet = 0; iGenJet < fNeroTree->genjetP4->GetEntries(); iGenJet++) {
    TLorentzVector *tempGenJet = (TLorentzVector*) fNeroTree->genjetP4->At(iGenJet);

    if (deltaR(tempGenJet->Eta(), tempGenJet->Phi(), jetEta, jetPhi) < 0.4 &&
        fabs(tempGenJet->Pt() - jetPt) < (3 * res * jetPt)) {
      pleaseScale = true;
      genPt = tempGenJet->Pt();
      break;
    }
  }

  if (pleaseScale) {
    return toSmear * TMath::Max(Float_t(0.0), genPt + sf*(jetPt - genPt))/jetPt;
  }
  else {
    return toSmear * generator.Gaus(1,TMath::Sqrt(pow(TMath::Max(Float_t(1.0), sf),2) - 1) * res);
  }

}

#endif
