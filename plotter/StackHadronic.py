#!/usr/bin/env python

from Stack import plotter, ReadExceptionConfig, MakePlots

ReadExceptionConfig('hadronic')

def SetupArgs():
    return [
        ['npv',50,0,50,'NPV','Events/1.0'],
        ['fatjet1MaxBTag',25,0,1.25,'#Delta #phi from MET','Events/1.0'],
        ['fatjet2MaxBTag',25,0,1.25,'#Delta #phi from MET','Events/1.0'],
        ['jet_ht',40,0,2000,'Jet HT (jet p_{T} > 30 GeV)','Events/1.0'],
        ['met',20,0,400,'MET [GeV]','Events/1.0'],
        ['mt',20,0,200,'m_{T}','Events/1.0'],
#        ['n_jetsTot',10,0,10,'Num Jets (p_{T} > 30 GeV)','Events/1.0'],
        ['n_jetsNotFat',10,0,10,'Num Jets (p_{T} > 30 GeV)','Events/1.0'],
#        ['n_bjetsLoose',6,0,6,'Num Loose b Jets','Events/1.0'],
#        ['n_bjetsMedium',6,0,6,'Num Medium b Jets','Events/1.0'],
#        ['n_bjetsTight',6,0,6,'Num Tight b Jets','Events/1.0'],
        ['fatjet1Pt',20,100,400,'p_{T} [GeV]','Events/1.0'],
        ['fatjet1Mass',25,0,250,'Fat Jet Mass [GeV]','Events/1.0'],
        ['fatjet1PrunedM',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjet1PrunedMuncorr',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjet1tau21',25,0,1.5,'#tau_{2}/#tau_{1}','Events/1.0'],
        ['fatjet1tau32',25,0,1.5,'#tau_{2}/#tau_{1}','Events/1.0'],
        ['fatjet1DRLooseB',25,0,5,'#Delta R from Loose b','Events/1.0'],
#        ['fatjet1DRMediumB',25,0,5,'#Delta R from Medium b','Events/1.0'],
#        ['fatjet1DRTightB',25,0,5,'#Delta R from Tight b','Events/1.0'],
        ['fatjet2Pt',20,100,400,'p_{T} [GeV]','Events/1.0'],
        ['fatjet2Mass',25,0,250,'Fat Jet Mass [GeV]','Events/1.0'],
        ['fatjet2PrunedM',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjet2PrunedMuncorr',25,0,250,'Fat Jet Pruned Mass [GeV]','Events/1.0'],
        ['fatjet2tau21',25,0,1.5,'#tau_{2}/#tau_{1}','Events/1.0'],
        ['fatjet2tau32',25,0,1.5,'#tau_{2}/#tau_{1}','Events/1.0'],
        ['fatjet2DRLooseB',25,0,5,'#Delta R from Loose b','Events/1.0'],
#        ['fatjet2DRMediumB',25,0,5,'#Delta R from Medium b','Events/1.0'],
#        ['fatjet2DRTightB',25,0,5,'#Delta R from Tight b','Events/1.0'],
        ]

def RunPlots(categories):
    cutList = ['full']
    MakePlots(categories,cutList,SetupArgs())
#    plotter.SetMakeRatio(False)
#    MakePlots(categories,cutList,[['fatjet2DRGenW',20,0,4,'#Delta R from Gen W','Events/1.0']])

if __name__ == '__main__':
    RunPlots(['hadronic'])
