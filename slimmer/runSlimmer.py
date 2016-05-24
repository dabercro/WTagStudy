#!/usr/bin/env python

import CrombieTools
import sys,os
import ROOT

OutTreeName = 'OutTree'

os.system(os.environ['CROMBIEPATH'] + '/scripts/MakeTree.sh ' + OutTreeName)
ROOT.gROOT.LoadMacro('NeroTree.C+')
ROOT.gROOT.LoadMacro(OutTreeName + '.cc+')
ROOT.gROOT.LoadMacro('slimmer.cc+')

# Load any other needed macros here

if len(sys.argv) == 1:
    exit()
if sys.argv[1] == 'test':
    ROOT.slimmer('root://eoscms//eos/cms/store/user/dabercro/Nero/v1.4/TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/TTJets_HT-2500toInf_TuneCUETP8M1/160523_184609/0000/NeroNtuples_2.root',
                 'test.root')
else:
    if not os.path.isfile(sys.argv[2]):
        ROOT.slimmer(sys.argv[1],
                     sys.argv[2])
    else:
        print sys.argv[2] + ' already exists!! Skipping...'
