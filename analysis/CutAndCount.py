#!/usr/bin/env python

from CrombieTools.PlotTools.PlotHists import plotter
from CrombieTools.LoadConfig import cuts
import os

env = os.environ

import ROOT
from ROOT import TFile

import sqlite3

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

listOfInt = []

for hist in hists:
    error = ROOT.Double()
    integral = hist.IntegralAndError(1,1,error)
    print('\nIntegral:    ' + str(integral))
    print('Uncertainty: ' + str(error))

    listOfInt.append({'integral' : float(integral), 'error' : float(error)})

data.Close()
mc.Close()

conn = sqlite3.connect('test.db')
cur  = conn.cursor()

cuts = ['none','mass','nsub','full']
cur.execute('create table yields (IsData, Cut, Yeild, Error)')

for index in range(len(listOfInt)):
    IsData = True
    if index % 2 == 1:
        IsData = False

    result = listOfInt[index]
    cur.execute('insert into yields values (?,?,?,?)', (IsData, cuts[index/2], result['integral'], result['error']))

conn.commit()
conn.close()
