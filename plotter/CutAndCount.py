#!/usr/bin/env python

from CrombieTools.AnalysisTools.HistAnalysis import *
from CrombieTools.LoadConfig import cuts
import os

SetupFromEnv()

histAnalysis.AddDataFile('wscale_Data.root')
histAnalysis.SetSignalName('W-matched (tt)')
histAnalysis.SetBaseCut(cuts.cut('semilep','full'))
histAnalysis.SetMCWeight('(' + cuts.defaultMCWeight + ' * xsec_v1 * ' + os.environ.get('CrombieLuminosity') + ')')

for cut, name in [('fatjetPrunedM > 60 && fatjetPrunedM < 110','Pruned Mass Cut'),
                  ('fatjettau21 < 0.6','$\\tau_2/\\tau_1$ Cut'),
                  ('fatjettau21 < 0.6 && fatjetPrunedM > 60 && fatjetPrunedM < 110','Full V-tag Cut')]:
    histAnalysis.AddScaleFactorCut(cut,name)

if __name__ == "__main__":
    histAnalysis.DoScaleFactors('n_tightlep',1,0,2)
