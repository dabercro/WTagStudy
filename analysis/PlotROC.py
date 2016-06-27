#!/usr/bin/env python

from CrombieTools.PlotTools.PlotROC import plotter

from ROOT import TFile

inDirectory = '/Users/dabercro/GradSchool/Summer16/bdtTest/'

sigFile  = TFile(inDirectory + 'wscale_TTJets.root')
backFile = TFile(inDirectory + 'wscale_QCD.root')

plotter.SetSignalTree(sigFile.events)
plotter.SetBackgroundTree(backFile.events)

theCut = '(n_looselep == 0 && jet_ht > 800 && fatjet1Pt > 350 && n_bjetsMedium == 2 && n_bjetsLoose == 2 && n_looselep == 0 && n_loosepho == 0 && n_jetsTot > 5 && fatjet2DRMediumB > 0.8 && fatjet2DRMediumB < 1.2) * (mcFactors * xsec_1)'

plotter.SetSignalCut(theCut)
plotter.SetBackgroundCut(theCut)

plotter.AddVar('fatjet1DPhiMet')
plotter.AddVar('fatjet1DRMediumB')

plotter.MakeCanvas('test')

sigFile.Close()
backFile.Close()
