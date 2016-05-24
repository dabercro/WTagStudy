#!/usr/bin/env python

from CrombieTools.PlotTools.PlotStack import *
from array import array
from cuts import regions

SetupFromEnv()

plotter.SetDebug(True)

plotter.SetStackLineWidth(2)
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

plotter.SetForceTop('W-matched (tt)')

def SetupArgs():
    return [
        ['met',20,0,400,'MET [GeV]','Events/1.0'],
        ['mt',20,0,200,'m_{T}','Events/1.0'],
        ['n_tightlep',4,0,4,'Num Tight Leptons','Events/1.0'],
        ['n_mediumlep',4,0,4,'Num Medium Leptons','Events/1.0'],
        ['n_jets ',10,0,10,'Num Jets (p_{T} > 30 GeV)','Events/1.0'],
        ['n_jetsSmall',10,0,10,'Num Jets (p_{T} > 30 GeV)','Events/1.0'],
        ['n_bjetsLoose',6,0,6,'Num Loose b Jets','Events/1.0'],
        ['n_bjetsMedium',6,0,6,'Num Medium b Jets','Events/1.0'],
        ['n_bjetsTight',6,0,6,'Num Tight b Jets','Events/1.0'],
        ['fatjet1Mass',25,0,250,'Fat Jet Mass [GeV]','Events/1.0'],
        ['fatjet1PrunedM',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjet1tau21',25,0,1.5,'#tau_{2}/#tau_{1}','Events/1.0'],
        ['fatjet2Mass',25,0,250,'Fat Jet Mass [GeV]','Events/1.0'],
        ['fatjet2PrunedM',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjet1DRGenW',20,0,4,'Delta R from Gen W','Events/1.0'],
        ['fatjet1DRLooseB',25,0,5,'Delta R from Loose b','Events/1.0'],
        ['fatjet1DRMediumB',25,0,5,'Delta R from Medium b','Events/1.0'],
        ['fatjet1DRTightB',25,0,5,'Delta R from Tight b','Events/1.0'],
        ['fatjet1DPhiLep1',25,0,5,'Delta phi from Lepton','Events/1.0'],
        ['topMass_11',25,0,500,'Reco Top Mass 1 [GeV]','Events/1.0'],
        ['topMass_12',25,0,500,'Reco Top Mass 2 [GeV]','Events/1.0'],
        ['topPrunedM_11',25,0,500,'Reco Top Mass 1 [GeV]','Events/1.0'],
        ['topPrunedM_12',25,0,500,'Reco Top Mass 2 [GeV]','Events/1.0'],
        ]

def RunPlots(categories):
    cutList = ['nocut','full']
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
#    MakePlots(categories,['full'],SetupArgs())

if __name__ == '__main__':
    RunPlots(['leading'])
