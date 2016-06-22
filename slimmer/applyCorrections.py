#!/usr/bin/env python

from CrombieTools.SkimmingTools import Corrector
from CrombieTools.Parallelization import RunOnDirectory
import os,sys

directory = sys.argv[1]

applicator = Corrector.MakeApplicator('mcFactors',True,'events','events',100000)

def addCorr(name,expr,cut,fileName,histName):
    applicator.AddCorrector(Corrector.MakeCorrector(name,expr,cut,fileName,histName))

addCorr('puWeight','npv','1','files/puWeight890pb.root','hPU')
#addCorr('puWeight','npv','1','files/puWeight_2fb_2016.root','puWeight')

applicator.AddFactorToMerge('mcWeight')
applicator.AddFactorToMerge('topPtReweighting')

applicator.SetInDirectory(directory)

if __name__ == "__main__":
    RunOnDirectory(applicator)
