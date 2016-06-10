#!/usr/bin/env python

from CrombieTools.PlotTools.PlotHists import plotter
from CrombieTools.LoadConfig import cuts
import math as m
import os

env = os.environ

import ROOT
from ROOT import TFile

data = TFile(env.get('CrombieInFilesDir') + '/wscale_Data.root')
mc   = TFile(env.get('CrombieInFilesDir') + '/res/wscale_TTJets.root')

factor = str(670.3 / mc.htotal.GetBinContent(1) * float(os.environ['CrombieLuminosity']))

dataTree = data.events
mcTree = mc.events

plotter.SetDefaultExpr('fatjet1DRLooseB')
plotter.AddTreeWeight(dataTree,cuts.cut('semilep','full'))
plotter.AddTreeWeight(mcTree,'(' + cuts.cut('semilep','full') + ') * (mcFactors * '+ factor +')')

plotter.AddTreeWeight(data.events,cuts.cut('semilep','full_massp'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('semilep','full_massp') + ') * (mcFactors * '+ factor +')')

plotter.AddTreeWeight(data.events,cuts.cut('semilep','full_tau21'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('semilep','full_tau21') + ') * (mcFactors * '+ factor +')')

plotter.AddTreeWeight(data.events,cuts.cut('semilep','full_tau21_massp'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('semilep','full_tau21_massp') + ') * (mcFactors * '+ factor +')')

hists = plotter.MakeHists(1,0,10)

ints = []
errs = []

for hist in hists:
    error = ROOT.Double()
    inte = hist.IntegralAndError(1,1,error)
    print('\nIntegral:    ' + str(inte))
    print('Uncertainty: ' + str(error))

    ints.append(inte)
    errs.append(error)

data.Close()
mc.Close()

for index in range(4):
    data  = ints[index*2]
    dataE = errs[index*2]

    mc  = ints[index*2 + 1]
    mcE = errs[index*2 + 1]

    print ('Norm ratio:')
    print (data/mc * ints[1]/ints[0])

    print ('Norm uncertainty:')
    print (m.sqrt(m.pow(dataE/mc,2) + m.pow(data/mc/mc*mcE,2)) * ints[1]/ints[0])
