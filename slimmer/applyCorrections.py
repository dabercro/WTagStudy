#!/usr/bin/env python

from CrombieTools.SkimmingTools import Corrector
from CrombieTools.Parallelization import RunOnDirectory
import os,sys

directory = sys.argv[1]

applicator = Corrector.MakeApplicator('mcFactors',True,'events','events',100000)

def addCorr(name,expr,cut,fileName,histName):
    applicator.AddCorrector(Corrector.MakeCorrector(name,expr,cut,fileName,histName))

addCorr('puWeight','npv','1','files/new_puWeights_13TeV_25ns.root','puWeights')

applicator.AddFactorToMerge('mcWeight')

applicator.SetInDirectory(directory)

RunOnDirectory(applicator)