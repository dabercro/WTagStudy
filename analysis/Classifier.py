#!/usr/bin/env python

from CrombieTools.AnalysisTools.TmvaClassifier import classifier

inDirectory = '/afs/cern.ch/work/d/dabercro/public/Summer16/bdtTest/'

classifier.SetConfigFile('config.txt')
classifier.SetUniformVariable('')
classifier.AddSignalTree(inDirectory + 'wscale_TTJets.root','events')
classifier.AddBackgroundTree(inDirectory + 'wscale_QCD.root','events')
classifier.SetWeight('(n_looselep == 0) * (mcFactors * xsec_1)')

classifier.TmvaClassify()

classifier.SetApplicationDirectory(inDirectory)

classifier.Apply()
