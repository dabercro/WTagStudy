#!/usr/bin/env python

from CrombieTools.PlotTools.PlotHists import plotter
from CrombieTools.LoadConfig import cuts
import os

env = os.environ

import ROOT
from ROOT import TFile

data = TFile(env.get('CrombieInFilesDir') + '/wscale_Data.root')
mc   = TFile(env.get('CrombieInFilesDir') + '/res/wscale_TTJets.root')

dataTree = data.events
mcTree = mc.events

plotter.SetDefaultExpr('fatjet1DRLooseB')
plotter.AddTreeWeight(dataTree,cuts.cut('semilep','full'))
plotter.AddTreeWeight(mcTree,'(' + cuts.cut('semilep','full') + ') * (mcFactors)')

plotter.AddTreeWeight(data.events,cuts.cut('semilep','full_massp'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('semilep','full_massp') + ') * (mcFactors)')

plotter.AddTreeWeight(data.events,cuts.cut('semilep','full_tau21'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('semilep','full_tau21') + ') * (mcFactors)')

plotter.AddTreeWeight(data.events,cuts.cut('semilep','full_tau21_massp'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('semilep','full_tau21_massp') + ') * (mcFactors)')

hists = plotter.MakeHists(1,0,10)

for hist in hists:
    error = ROOT.Double()
    print('\nIntegral:    ' + str(hist.IntegralAndError(1,1,error)))
    print('Uncertainty: ' + str(error))

data.Close()
mc.Close()
