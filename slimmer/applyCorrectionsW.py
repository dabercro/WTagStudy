#!/usr/bin/env python

from applyCorrections import *

addCorr('ewk_w','genBosPt','abs(genBosPdgId) == 24','files/puWeight890pb.root','hPU')

if __name__ == "__main__":
    RunOnDirectory(applicator)

