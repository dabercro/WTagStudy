#!/usr/bin/env python

import CrombieTools
import sys,os
import ROOT

OutTreeName = 'OutTree'

os.system('crombie maketree ' + OutTreeName)
ROOT.gROOT.LoadMacro('Nero_30fb.C+')
ROOT.gROOT.LoadMacro(OutTreeName + '.cc+')
ROOT.gROOT.LoadMacro('slimmer.cc+')

# Load any other needed macros here

if len(sys.argv) == 1:
    exit()
if sys.argv[1] == 'test':
    ROOT.slimmer(
#        'root://eoscms//store/user/dabercro/Nero/80X/SingleMuon/SingleMuon_0/160907_133042/0000/NeroNtuples_90.root',
        'root://eoscms.cern.ch//store/group/phys_higgs/ceballos/setup80x_ichep/Data/Nero/v2.0/SingleMuon/SingleMuon-Run2016E-23Sep2016/161208_212714/0000/NeroNtuples_10.root',
        'test.root')

if len(sys.argv) < 3:
    exit()
else:
    if not os.path.isfile(sys.argv[2]):
        ROOT.slimmer(sys.argv[1],
                     sys.argv[2])
    else:
        print sys.argv[2] + ' already exists!! Skipping...'
