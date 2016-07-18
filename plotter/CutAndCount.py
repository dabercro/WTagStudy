#!/usr/bin/env python

from CrombieTools.AnalysisTools.HistAnalysis import *
from CrombieTools.LoadConfig import cuts
import os

SetupFromEnv()

histAnalysis.SetIsPresentation(False)

histAnalysis.AddDataFile('wscale_Data.root')
histAnalysis.SetSignalName('Signal')
histAnalysis.SetMCWeight('(' + cuts.defaultMCWeight + ' * xsec_v1 * ' + os.environ.get('CrombieLuminosity') + ')')


def doBoth(addToRegion=''):
    print('All mass')
    histAnalysis.SetBaseCut(cuts.cut('semilep','full' + addToRegion))
    histAnalysis.DoScaleFactors('n_tightlep',1,0,2)
    print('No low mass')
    histAnalysis.SetBaseCut(cuts.cut('nolowmass','full' + addToRegion))
    histAnalysis.DoScaleFactors('n_tightlep',1,0,2)


def doSmear(whichDir, addToRegion=''):
    histAnalysis.ResetScaleFactorCuts()
    for name, cut in [('Pruned Mass Cut',cuts.regionCuts['massp']),
                      ('$\\tau_2/\\tau_1$ Cut',cuts.regionCuts['tau21']),
                      ('Full V-tag Cut',cuts.joinCuts(['massp','tau21']))]:
        datacut = '(' + cut + ' && fatjetPt > 250)'
        mccut = '(' + cut.replace('L2L3','L2L3Smeared' + whichDir) + ' && fatjetPtSmeared' + whichDir + '  > 250)'
        histAnalysis.AddScaleFactorCut(name, mccut, datacut)

    doBoth(addToRegion + '_nopt')


def GetTables(addToRegion=''):
    histAnalysis.ResetScaleFactorCuts()
    for name, cut in [('Pruned Mass Cut',cuts.regionCuts['massp']),
                      ('$\\tau_2/\\tau_1$ Cut',cuts.regionCuts['tau21']),
                      ('Full V-tag Cut',cuts.joinCuts(['massp','tau21']))]:
        histAnalysis.AddScaleFactorCut(name, cut)

    print('\nDefault Pythia setup\n')
    doBoth(addToRegion)

#    print('\nSmear Down\n')
#    doSmear('Down', addToRegion)
#    print('\nSmear Central\n')
#    doSmear('Central', addToRegion)
#    print('\nSmear Up\n')
#    doSmear('Up', addToRegion)


def main():
    GetTables()
#    for move in range(10):
#        print('\nAbout to do range ' + str(move) + '\n')
#        GetTables('_' + str(move * 0.1))


if __name__ == "__main__":
    main()
