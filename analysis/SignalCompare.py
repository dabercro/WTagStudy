#!/usr/bin/env python

from CrombieTools.PlotTools.PlotHists import plotter

from ROOT import TFile

theFile = TFile('signalTest.root')

plotter.SetDefaultTree(theFile.Get('events'))
plotter.SetDefaultExpr('fatjetPrunedML2L3')

weight = 'fatjetPt > 250 && n_looselep == 0 && n_loosepho == 0 && n_bjetsLoose == 0 && met > 250'

plotter.AddWeight(weight)
plotter.AddWeight(weight + ' && fatjetDRWq2 > 0 && fatjetDRWq1 > 0.8')
plotter.AddWeight(weight + ' && fatjetDRWq2 > 0.8 && fatjetDRWq1 > 0.8')

plotter.AddLegendEntry('All',1)
plotter.AddLegendEntry('Part of W',2)
plotter.AddLegendEntry('Not Matching W',4)

plotter.MakeCanvas("plots/fatjetPrunedMx",25,0,150,"m_{pruned} [GeV]","A.U.")
