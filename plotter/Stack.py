#!/usr/bin/env python

from CrombieTools.PlotTools.PlotStack import *
from array import array
from cuts import regions

SetupFromEnv()

plotter.SetMakeRatio(False)
plotter.SetIsCMSPrelim(True)
plotter.SetTreeName('events')
plotter.SetAllHistName('htotal')
plotter.AddDataFile('wscale_Data.root')
plotter.SetLegendLocation(plotter.kUpper,plotter.kRight,0.25,0.5)
plotter.SetEventsPer(1.0)
plotter.SetMinLegendFrac(0.03)
plotter.SetIgnoreInLinear(0.005)
plotter.SetOthersColor(922)
plotter.SetFontSize(0.03)
plotter.SetAxisTitleOffset(1.2)

plotter.SetForceTop('Resonant top')

def SetupArgs():
    return [
        ['mt',40,0,200,'m_{T}','AU'],
        ['n_tightlep',4,0,4,'Num Tight Leptons','AU'],
        ['n_mediumlep',4,0,4,'Num Medium Leptons','AU'],
        ['n_jets',20,0,20,'Num Jets (p_{T} > 30 GeV)','AU'],
        ['n_bjetsLoose',6,0,6,'Num Loose b Jets','AU'],
        ['n_bjetsMedium',6,0,6,'Num Medium b Jets','AU'],
        ['n_bjetsTight',6,0,6,'Num Tight b Jets','AU'],
        ['fatjet1Mass',50,0,250,'Fat Jet Mass [GeV]','AU'],
        ['fatjet1PrunedM',50,0,250,'Fat Jet Pruned Mass [GeV]','AU'],
        ['fatjet1tau21',50,0,1.5,'#tau_{2}/#tau_{1}','AU'],
        ['fatjet1DRGenW',20,0,4,'Delta R from Gen W','AU'],
        ['fatjet1DRLooseB',25,0,5,'Delta R from Loose b','AU'],
        ['fatjet1DRMediumB',25,0,5,'Delta R from Medium b','AU'],
        ['fatjet1DRTightB',25,0,5,'Delta R from Tight b','AU'],
        ['fatjet1DPhiLep1',25,0,5,'Delta phi from Lepton','AU'],
        ['topMass_11',40,0,500,'Reco Top Mass 1 [GeV]','AU'],
        ['topMass_12',40,0,500,'Reco Top Mass 2 [GeV]','AU'],
        ['topPrunedM_11',40,0,500,'Reco Top Mass 1 [GeV]','AU'],
        ['topPrunedM_12',40,0,500,'Reco Top Mass 2 [GeV]','AU'],
        ['fatjet2PrunedM',50,0,250,'Fat Jet Pruned Mass [GeV]','AU'],
        ['fatjet2tau21',30,0,1.5,'tau_{2}/$tau_{1}','AU'],
        ['fatjet2DRGenW',20,0,4,'Delta R from Gen W','AU'],
        ['fatjet2DRLooseB',25,0,4,'Delta R from Loose b','AU'],
        ['fatjet2DRMediumB',25,0,4,'Delta R from Medium b','AU'],
        ['fatjet2DRTightB',25,0,4,'Delta R from Tight b','AU'],
        ['fatjet2DPhiLep1',25,0,5,'Delta phi from Lepton','AU'],
        ['topMass_21',40,0,500,'Reco Top Mass 1 [GeV]','AU'],
        ['topMass_22',40,0,500,'Reco Top Mass 2 [GeV]','AU'],
        ['topPrunedM_21',40,0,500,'Reco Top Mass 1 [GeV]','AU'],
        ['topPrunedM_22',40,0,500,'Reco Top Mass 2 [GeV]','AU']
        ]

def RunPlots(categories):
    cutList = ['nocut']
    for region in regions:
        cutList.append(region)
        tempList1 = regions[:regions.index(region)]
        for region1 in tempList1:
            cutList.append(region1 + '_' + region)
            tempList2 = tempList1[:tempList1.index(region1)]
            for region2 in tempList2:
                cutList.append(region2 + '_' + region1 + '_' + region)
                tempList3 = tempList2[:tempList2.index(region2)]
                for region3 in tempList3:
                    cutList.append(region3 + '_' + region2 + '_' + region1 + '_' + region)

    MakePlots(categories,cutList,SetupArgs())

if __name__ == '__main__':
    RunPlots(['leading'])
