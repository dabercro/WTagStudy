#!/usr/bin/env python

from CrombieTools.PlotTools.PlotHists import plotter

from ROOT import TFile

directory = '/Users/dabercro/GradSchool/Summer16/Skim_160622/'
theFile = TFile(directory + 'wscale_TTJets_SingleLeptFromT.root')

plotter.SetDefaultExpr('topPtReweighting')
plotter.SetDefaultTree(theFile.Get('events'))

plotter.AddWeight('fatjetPt > 250 && thirdFatMass < 50 && n_tightlep == 1 && n_looselep == 1 && n_bjetsLoose > 0 && fatjetDRLooseB > 0.8 && fatjetDRLooseB < 1.2 && fatjetDPhiLep1 > 2.0 && ((n_jetsNotFat == 3 && fatjet2Pt < 0) || (n_jetsNotFat == 2)) && n_tightlep == 1 && n_looselep == 1 && fatjet1DRGenW < 0.2')
plotter.AddWeight('fatjetPt > 250 && thirdFatMass < 50 && n_tightlep == 1 && n_looselep == 1 && n_bjetsLoose > 0 && fatjetDRLooseB > 0.8 && fatjetDRLooseB < 1.2 && fatjetDPhiLep1 > 2.0 && n_tightlep == 1 && n_looselep == 1 && fatjet1DRGenW < 0.2')

plotter.AddLegendEntry('With n_{jets} cut',1)
plotter.AddLegendEntry('Without that cut',2)

plotter.SetRatioIndex(1)

plotter.MakeCanvas("topPtWeight",50,0.75,1.2,"top p_{T} reweighting","A.U.")
