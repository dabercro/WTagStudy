#!/usr/bin/env python

from CrombieTools.AnalysisTools.HistAnalysis import *
from CrombieTools.LoadConfig import cuts
import os

SetupFromEnv()

histAnalysis.AddDataFile('wscale_Data.root')
histAnalysis.SetSignalName('Signal')
histAnalysis.SetMCWeight('(' + cuts.defaultMCWeight + ' * xsec_v1 * ' + os.environ.get('CrombieLuminosity') + ')')

for cut, name in [(cuts.regionCuts['massp'],'Pruned Mass Cut'),
                  (cuts.regionCuts['tau21'],'$\\tau_2/\\tau_1$ Cut'),
                  (cuts.joinCuts(['massp','tau21']),'Full V-tag Cut')]:
    histAnalysis.AddScaleFactorCut(cut,name)

if __name__ == "__main__":
    histAnalysis.SetBaseCut(cuts.cut('semilep','full_ntau_mediumB_ntot'))
    histAnalysis.DoScaleFactors('n_tightlep',1,0,2) #,0,False)
    histAnalysis.SetBaseCut(cuts.cut('nolowmass','full_ntau_mediumB_ntot'))
    histAnalysis.DoScaleFactors('n_tightlep',1,0,2) #,0,False)
