#!/usr/bin/env python

from CrombieTools.AnalysisTools.HistAnalysis import *
from CrombieTools.LoadConfig import cuts
import os

SetupFromEnv()

histAnalysis.AddDataFile('../Skim_170116/wscale_Data.root')
histAnalysis.SetBaseCut(cuts.cut('semilep','nocut'))
histAnalysis.SetMCWeight('(mcFactors/puWeight)')

histAnalysis.MakeReweightHist('puWeight_30fb_2016.root', 'puWeight', 'npv', 40, 0, 40)
