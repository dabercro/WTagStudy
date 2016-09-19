#!/usr/bin/env python

import CrombieTools
import sys,os
import ROOT

OutTreeName = 'OutTree'

os.system('crombie maketree ' + OutTreeName)
ROOT.gROOT.LoadMacro('NeroTree.C+')
ROOT.gROOT.LoadMacro(OutTreeName + '.cc+')
ROOT.gROOT.LoadMacro('slimmer.cc+')

# Load any other needed macros here

if len(sys.argv) == 1:
    exit()
if sys.argv[1] == 'test':
    ROOT.slimmer(
        'root://eoscms//store/user/dabercro/Nero/80X/SingleMuon/SingleMuon_0/160907_133042/0000/NeroNtuples_90.root',
        'test.root')

if len(sys.argv) < 3:
    exit()
else:
    if not os.path.isfile(sys.argv[2]):
        ROOT.slimmer(sys.argv[1],
                     sys.argv[2])
    else:
        print sys.argv[2] + ' already exists!! Skipping...'
