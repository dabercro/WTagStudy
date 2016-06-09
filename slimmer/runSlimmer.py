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
    ROOT.slimmer(
        'root://eoscms//eos/cms/store/user/zdemirag/setup80x/Nero/v1.4/JetHT/JetHT-Run2016B-v2/160606_232337/0000/NeroNtuples_70.root',
#        'root://eoscms//eos/cms/store/user/zdemirag/setup80x/Nero/v1.4/TT_TuneCUETP8M1_13TeV-powheg-pythia8/TT_TuneCUETP8M1_13TeV-powheg/160606_230204/0000/NeroNtuples_70.root',
#        'root://eosuser//eos/user/d/dabercro/SingleLeptonData_76X_V001/SingleMuon/SingleMuon-Run2015D/160523_184442/0000/NeroNtuples_66.root',
        'test.root')

if len(sys.argv) < 3:
    exit()
else:
    if not os.path.isfile(sys.argv[2]):
        ROOT.slimmer(sys.argv[1],
                     sys.argv[2])
    else:
        print sys.argv[2] + ' already exists!! Skipping...'
