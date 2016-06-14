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
back1 = TFile(env.get('CrombieInFilesDir') + '/nonres/wscale_TTJets.root')
back2 = TFile(env.get('CrombieInFilesDir') + '/probtop/wscale_TTJets.root')

factor = str(834.0 / mc.htotal.GetBinContent(1) * float(os.environ['CrombieLuminosity']))

dataTree = data.events
mcTree = mc.events
back1Tree = back1.events
back2Tree = back2.events

plotter.SetDefaultExpr('fatjet1DRLooseB')
plotter.AddTreeWeight(dataTree,cuts.cut('nolowmass','full'))
plotter.AddTreeWeight(mcTree,'(' + cuts.cut('nolowmass','full') + ') * (mcFactors * '+ factor +')')

plotter.AddTreeWeight(data.events,cuts.cut('nolowmass','full_massp'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('nolowmass','full_massp') + ') * (mcFactors * '+ factor +')')

plotter.AddTreeWeight(data.events,cuts.cut('nolowmass','full_tau21'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('nolowmass','full_tau21') + ') * (mcFactors * '+ factor +')')

plotter.AddTreeWeight(data.events,cuts.cut('nolowmass','full_tau21_massp'))
plotter.AddTreeWeight(mc.events,'(' + cuts.cut('nolowmass','full_tau21_massp') + ') * (mcFactors * '+ factor +')')

plotter.AddTreeWeight(back1Tree,'(' + cuts.cut('nolowmass','full') + ') * (mcFactors * '+ factor +')')
plotter.AddTreeWeight(back1Tree,'(' + cuts.cut('nolowmass','full_massp') + ') * (mcFactors * '+ factor +')')
plotter.AddTreeWeight(back1Tree,'(' + cuts.cut('nolowmass','full_tau21') + ') * (mcFactors * '+ factor +')')
plotter.AddTreeWeight(back1Tree,'(' + cuts.cut('nolowmass','full_tau21_massp') + ') * (mcFactors * '+ factor +')')

plotter.AddTreeWeight(back2Tree,'(' + cuts.cut('nolowmass','full') + ') * (mcFactors * '+ factor +')')
plotter.AddTreeWeight(back2Tree,'(' + cuts.cut('nolowmass','full_massp') + ') * (mcFactors * '+ factor +')')
plotter.AddTreeWeight(back2Tree,'(' + cuts.cut('nolowmass','full_tau21') + ') * (mcFactors * '+ factor +')')
plotter.AddTreeWeight(back2Tree,'(' + cuts.cut('nolowmass','full_tau21_massp') + ') * (mcFactors * '+ factor +')')


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

table_data = ['Background Subtracted Data']
table_mc   = ['W-matched MC']
table_rat  = ['Normalized Ratio']

fmt = '{0:.2f}'

scaleMC = (ints[1] + ints[8] + ints[12])/ints[0]
#scaleMC = 1.0
uncpercent = 1.0

for index in range(4):
    data  = ints[index*2] - (ints[index + 8] + ints[index + 12])/scaleMC
    dataE = m.sqrt(m.pow(errs[index*2],2) + m.pow(errs[index + 8]/scaleMC,2) + m.pow(errs[index + 12]/scaleMC,2)) + \
        uncpercent * (ints[index + 8] + ints[index + 12])/scaleMC

    table_data.append(fmt.format(data) + ' \pm ' + fmt.format(dataE))

    mc  = ints[index*2 + 1]
    mcE = errs[index*2 + 1]

    table_mc.append(fmt.format(mc) + ' \pm ' + fmt.format(mcE))

    print ('Norm ratio:')
    rat = (data/mc * ints[1]/(ints[0] - (ints[8] + ints[12])/scaleMC))
    print (rat)

    print ('Norm uncertainty:')
    ratE = (m.sqrt(m.pow(dataE/mc,2) + m.pow(data/mc/mc*mcE,2)) * ints[1]/(ints[0] - (ints[8] + ints[12])/scaleMC))
    print (ratE)

    table_rat.append(fmt.format(rat) + ' \pm ' + fmt.format(ratE))

for row in [table_data, table_mc, table_rat]:
    print(' & '.join(row) + ' \\\\')
