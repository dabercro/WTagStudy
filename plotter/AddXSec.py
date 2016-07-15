#!/usr/bin/env python

from CrombieTools.AnalysisTools.XSecAdder import RunXSecAdder as run
import sys

run(*([sys.argv[1]]))
run(*([sys.argv[1],'herwig']))
