#!/usr/bin/env python

from CrombieTools.AnalysisTools.HistAnalysis import *
from CrombieTools.LoadConfig import cuts
import os

SetupFromEnv()

histAnalysis.AddDataFile('wscale_Data.root')
histAnalysis.SetBaseCut(cuts.cut('semilep','nocut'))
histAnalysis.SetMCWeight('(mcWeight * XSecWeight * ' + os.environ.get('CrombieLuminosity') + ')')

histAnalysis.MakeReweightHist('puWeight_2fb_2016.root','puWeight','npv',35,0,35)
