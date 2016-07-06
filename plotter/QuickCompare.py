#!/usr/bin/env python

from CrombieTools.PlotTools.PlotHists import plotter
from CrombieTools.LoadConfig import cuts

from ROOT import TFile

directory = '/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_160704/nonres/'

aFile = TFile(directory + 'wscale_TT_TuneCUETP8M1_13TeV-powheg-pythia8.root')
bFile = TFile(directory + 'wscale_TT_TuneEE5C_13TeV-powheg-herwigpp.root')

plotter.AddTree(aFile.Get('events'))
plotter.AddTree(bFile.Get('events'))

plotter.SetNormalizedHists(True)

plotter.SetDefaultExpr('fatjetPrunedM')
plotter.SetDefaultWeight('(' + cuts.cut('semilep','full') + ')*(' + cuts.defaultMCWeight + ')')

plotter.AddLegendEntry('Pythia 8',1)
plotter.AddLegendEntry('Herwig',2)

plotter.MakeCanvas('powheg_showerComparison_nonres',25,0,250,"m_{pruned} [GeV]","A.U.")
