#!/usr/bin/env python

from CutAndCount import *

histAnalysis.SetBaseCut(cuts.cut('nolowmass','full'))

if __name__ == "__main__":
    histAnalysis.DoScaleFactors('n_tightlep',1,0,2)
