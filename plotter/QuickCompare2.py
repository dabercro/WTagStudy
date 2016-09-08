#!/usr/bin/env python

from CrombieTools.PlotTools.PlotHists import plotter
from CrombieTools.LoadConfig import cuts

from ROOT import TFile, TChain

aFile = TFile('/afs/cern.ch/work/d/dabercro/public/Summer16/MonoX/monojet/slimmer/fullsim80x.root')

signal_loc = '/afs/cern.ch/work/d/dabercro/public/Summer16/74x_signal/'
cChain = TChain('events','events_chainc')
cChain.Add(signal_loc + 'monojet_VectorMonoW_Mphi-2000_Mchi-50_gSM-1p0_gDM-1p0_13TeV.root')
#cChain.Add(signal_loc + 'monojet_AxialMonoW_Mphi-2000_Mchi-50_gSM-1p0_gDM-1p0_13TeV.root')
#cChain.Add(signal_loc + 'monojet_VectorMonoZ_Mphi-2000_Mchi-50_gSM-1p0_gDM-1p0_13TeV.root')

plotter.AddTree(aFile.Get('events'))
plotter.AddTree(cChain)

plotter.SetRatioIndex(0)

#plotter.SetNormalizedHists(True)

plotter.AddWeight('(fatjet1Pt > 0) * mcWeight * 2.450')
plotter.AddWeight('(fatjet1Pt > 0) * mcWeight * 2.058')

plotter.AddLegendEntry('Axial 2000 #rightarrow 50 80X',1,2,1)
plotter.AddLegendEntry('Axial 2000 #rightarrow 50 74X',2,2,2)

plotter.SetLegendLocation(plotter.kUpper,plotter.kRight,0.4,0.3)

plotter.SetDefaultExpr('fatjet1Pt')
plotter.MakeCanvas('~/www/plots/160728/compare_releases_pT',30,250,1000,"p_{T} [GeV]","A.U.")
plotter.SetDefaultExpr('fatjet1PrunedM')
plotter.MakeCanvas('~/www/plots/160728/compare_releases_masspruned',20,0,200,"m_{pruned} [GeV]","A.U.")
plotter.SetDefaultExpr('fatjet1Mass')
plotter.MakeCanvas('~/www/plots/160728/compare_releases_mass',25,0,250,"m_{raw} [GeV]","A.U.")
plotter.SetDefaultExpr('met')
plotter.MakeCanvas('~/www/plots/160728/compare_releases_met',30,250,1000,"E_{T}^{miss} [GeV]","A.U.")
plotter.SetLegendLocation(plotter.kUpper,plotter.kLeft,0.4,0.3)
plotter.SetDefaultExpr('fatjet1tau21')
plotter.MakeCanvas('~/www/plots/160728/compare_releases_tau21',24,-0.2,1.0,"#tau_{2}/#tau_{1}","A.U.")
