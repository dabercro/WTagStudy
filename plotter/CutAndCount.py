#!/usr/bin/env python

from CrombieTools.AnalysisTools.HistAnalysis import *
from CrombieTools.LoadConfig import cuts
import os, sys

SetupFromEnv()

histAnalysis.SetPrintingMethod(histAnalysis.kPresentation)

histAnalysis.ResetConfig()
histAnalysis.ReadMCConfig('MCBackground.txt')
histAnalysis.AddDataFile('wscale_Data.root')
histAnalysis.SetSignalName('Signal')
histAnalysis.SetSearchBy(histAnalysis.kLegendEntry)
histAnalysis.SetMCWeight(cuts.defaultMCWeight)


def doBoth(addToRegion='', **kwargs):
    print('All mass')
    if addToRegion == '_nopt':
        histAnalysis.SetBaseCut(cuts.cut('semilep','full' + addToRegion) + ' && fatjetPtSmeared' + kwargs['which'] + ' > 250',
                                cuts.cut('semilep','full' + addToRegion) + ' && fatjetPt > 250')
    else:
        histAnalysis.SetBaseCut(cuts.cut('semilep','full' + addToRegion))
    histAnalysis.DoScaleFactors('n_tightlep',1,0,2)
    print('No low mass')

    if addToRegion == '_nopt':
        histAnalysis.SetBaseCut(cuts.cut('nolowmass','full' + addToRegion) + ' && fatjetPtSmeared' + kwargs['which'] + ' > 250',
                                cuts.cut('nolowmass','full' + addToRegion) + ' && fatjetPt > 250')
    else:
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

    doBoth(addToRegion + '_nopt', which=whichDir)


def GetTables(addToRegion=''):
    histAnalysis.ResetScaleFactorCuts()
    for name, cut in [('Pruned Mass Cut',cuts.regionCuts['massp']),
                      ('$\\tau_2/\\tau_1$ Cut',cuts.regionCuts['tau21']),
                      ('Full V-tag Cut',cuts.joinCuts(['massp','tau21']))]:
        histAnalysis.AddScaleFactorCut(name, cut)

    doBoth(addToRegion)


def printBig(printThis):
    chars = len(printThis)
    print('\n' + '#' * (chars + 4))
    print('# {0} #'.format(printThis))
    print('#' * (chars + 4) + '\n')



if __name__ == "__main__":
    GetTables()

    if len(sys.argv) > 1 and sys.argv[1] == 'full':

        printBig('TOP WEIGHT')

        print('\nNo Top\n')
        histAnalysis.SetMCWeight('%s/topPtReweighting' % cuts.defaultMCWeight)
        GetTables()
        print('\nTop Squared\n')
        histAnalysis.SetMCWeight('%s*topPtReweighting' % cuts.defaultMCWeight)
        GetTables()

        histAnalysis.SetMCWeight(cuts.defaultMCWeight)

        printBig('SMEARING')

        print('\nSmear Down\n')
        doSmear('Down')
        print('\nSmear Central\n')
        doSmear('Central')
        print('\nSmear Up\n')
        doSmear('Up')
        
        printBig('BACKGROUND SCALING')

        print('\nBackground Up\n')
        histAnalysis.ChangeBackground(1.0)
        GetTables()
        print('\nBackground Down\n')
        histAnalysis.ChangeBackground(-0.5)
        doBoth()
        histAnalysis.ChangeBackground(0.0)

        printBig('HIGH PT')

        print('\nHigh Pt\n')
        doBoth('_highpt')
        
        printBig('SHOWERING UNCERTAINTY')

        for move in range(10):
            print('\nAbout to do range ' + str(move) + '\n')
            GetTables('_' + str(move * 0.1))

        printBig('ALTERNATE BACKGROUNDS')

        print('\nMore background\n')
        histAnalysis.ResetConfig()
        histAnalysis.AddDataFile('wscale_Data.root')
        histAnalysis.ReadMCConfig('MCBackground_more.txt')
        GetTables()
        print('\nMid background\n')
        histAnalysis.ResetConfig()
        histAnalysis.AddDataFile('wscale_Data.root')
        histAnalysis.ReadMCConfig('MCBackground_mid.txt')
        doBoth()
