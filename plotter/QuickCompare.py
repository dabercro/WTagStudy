#!/usr/bin/env python

from CrombieTools.PlotTools.PlotHists import plotter
from CrombieTools.LoadConfig import cuts

from ROOT import TFile, TChain

directory = '/afs/cern.ch/work/d/dabercro/public/Summer16/Full_160701/'

aChain = TChain('events','events_chaina')
aChain.Add('/afs/cern.ch/work/d/dabercro/eosuser/user/d/dabercro/Winter15Flat/FullOut_160221/monojet_JHUGen_Higgs_WH_125_10.root')
aChain.Add('/afs/cern.ch/work/d/dabercro/eosuser/user/d/dabercro/Winter15Flat/FullOut_160221/monojet_JHUGen_Higgs_ZH_125_10.root')

signal_loc = '/afs/cern.ch/work/d/dabercro/public/Summer16/74x_signal/'
bChain = TChain('events','events_chainb')
bChain.Add(signal_loc + 'monojet_VectorMonoW_Mphi-500_Mchi-50_gSM-1p0_gDM-1p0_13TeV.root')
bChain.Add(signal_loc + 'monojet_VectorMonoZ_Mphi-500_Mchi-50_gSM-1p0_gDM-1p0_13TeV.root')

cChain = TChain('events','events_chainc')
cChain.Add(signal_loc + 'monojet_VectorMonoW_Mphi-2000_Mchi-50_gSM-1p0_gDM-1p0_13TeV.root')
cChain.Add(signal_loc + 'monojet_VectorMonoZ_Mphi-2000_Mchi-50_gSM-1p0_gDM-1p0_13TeV.root')

dFile = TFile(directory + 'wscale_TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root')

plotter.AddTree(aChain)
plotter.AddTree(bChain)
plotter.AddTree(cChain)
plotter.AddTree(dFile.Get('events'))

plotter.SetNormalizedHists(True)

plotter.AddExpr('fatjet1Pt')
plotter.AddExpr('fatjet1Pt')
plotter.AddExpr('fatjet1Pt')
plotter.AddExpr('fatjetPt')
plotter.AddWeight('mcWeight')
plotter.AddWeight('mcWeight')
plotter.AddWeight('mcWeight')
plotter.AddWeight('(' + cuts.cut('semilep','full') + ')*(mcWeight)')

plotter.AddLegendEntry('VH Signal',1,2,1)
plotter.AddLegendEntry('m_{#phi} = 500 GeV Signal',2,2,2)
plotter.AddLegendEntry('m_{#phi} = 2000 GeV Signal',3,2,3)
plotter.AddLegendEntry('W in tt',4,2,4)

plotter.MakeCanvas('~/www/plots/160707/WPt_comparison',17,275,700,"p_{T} [GeV]","A.U.")
