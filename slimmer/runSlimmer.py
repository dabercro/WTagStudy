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

if sys.argv[1] == "compile":
    exit()
else:
    if not os.path.isfile(sys.argv[2]):
        ROOT.slimmer(sys.argv[1],
                     sys.argv[2])
    else:
        print sys.argv[2] + " already exists!! Skipping..."
