#!/usr/bin/env python

from CrombieTools.PlotTools.PlotStack import *
from array import array

SetupFromEnv()

#plotter.SetDebug(True)

plotter.SetStackLineWidth(2)
plotter.SetIsCMSPrelim(True)
plotter.SetTreeName('events')
plotter.SetAllHistName('htotal')
plotter.SetLegendLocation(plotter.kUpper,plotter.kRight,0.25,0.5)
plotter.SetEventsPer(1.0)
plotter.SetMinLegendFrac(0.0)
plotter.SetIgnoreInLinear(0.005)
plotter.SetOthersColor(922)
plotter.SetFontSize(0.03)
plotter.SetAxisTitleOffset(1.2)
plotter.SetRatioMinMax(0,2)

plotter.SetForceTop('W-matched (tt)')

def SetupArgs():
    return [
        ['npv',50,0,50,'NPV','Events/1.0'],
        ['fatjetMaxBTag',25,0,1.25,'Max subjet b-tag (csv)','Events/1.0'],
#        ['jet_ht',40,0,2000,'Jet HT (jet p_{T} > 30 GeV)','Events/1.0'],
#        ['fatjetDPhiMet',25,0,5,'#Delta #phi from MET','Events/1.0'],
        ['met',20,0,400,'MET [GeV]','Events/1.0'],
        ['mt',20,0,200,'m_{T}','Events/1.0'],
        ['n_tightlep',4,0,4,'Num Tight Leptons','Events/1.0'],
#        ['n_mediumlep',4,0,4,'Num Medium Leptons','Events/1.0'],
        ['n_jetsTot',10,0,10,'Num Jets (p_{T} > 30 GeV)','Events/1.0'],
        ['n_jetsNotFat',10,0,10,'Num Jets (p_{T} > 30 GeV)','Events/1.0'],
        ['n_bjetsLoose',6,0,6,'Num Loose b Jets','Events/1.0'],
        ['n_bjetsMedium',6,0,6,'Num Medium b Jets','Events/1.0'],
        ['n_bjetsTight',6,0,6,'Num Tight b Jets','Events/1.0'],
        ['fatjetPt',25,100,600,'p_{T} [GeV]','Events/1.0'],
        ['fatjetPtSmearedCentral',25,100,600,'p_{T} [GeV]','Events/1.0'],
        ['fatjetPtSmearedUp',25,100,600,'p_{T} [GeV]','Events/1.0'],
        ['fatjetPtSmearedDown',25,100,600,'p_{T} [GeV]','Events/1.0'],
        ['fatjetMass',25,0,250,'Fat Jet Mass [GeV]','Events/1.0'],
#        ['fatjetPrunedM',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjetPrunedML2L3',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjetPrunedML2L3','fatjetPrunedML2L3SmearedCentral',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjetPrunedML2L3','fatjetPrunedML2L3SmearedUp',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjetPrunedML2L3','fatjetPrunedML2L3SmearedDown',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
#        ['fatjetPrunedMuncorr',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjettau21',25,0,1.5,'#tau_{2}/#tau_{1}','Events/1.0'],
#        ['fatjettau32',25,0,1.5,'#tau_{2}/#tau_{1}','Events/1.0'],
        ['fatjetDRLooseB',25,0,5,'#Delta R from Loose b','Events/1.0'],
#        ['fatjetDRMediumB',25,0,5,'#Delta R from Medium b','Events/1.0'],
#        ['fatjetDRTightB',25,0,5,'#Delta R from Tight b','Events/1.0'],
        ['fatjetDPhiLep1',25,0,5,'#Delta #phi from Lepton','Events/1.0'],
        ]

def RunPlots(categories):
    cutList = ['nocut','nocut_ntot_nsmalljets','full','full_highpt','full_massp_tau21']
    for move in range(8):
        cutList.append('full_' + str(move * 0.1))

    MakePlots(categories,cutList,SetupArgs())
    plotter.SetMakeRatio(False)
    MakePlots(categories,cutList,[['fatjetDRGenW',25,0,5,'#Delta R from Gen W','Events/1.0']])

if __name__ == '__main__':
    plotter.AddDataFile('wscale_Data.root')
    RunPlots(['semilep'])
