#!/usr/bin/env python

from applyCorrections import *

addCorr('ewk_w','genBosPt','abs(genBosPdgId) == 24','files/uncertainties_EWK_24bins.root',['EWKcorr/W','WJets_012j_NLO/nominal'])
addCorr('kfactor_w','genBosPt','abs(genBosPdgId) == 24','files/uncertainties_EWK_24bins.root',['WJets_012j_NLO/nominal','WJets_LO/inv_pt'])

if __name__ == "__main__":
    RunOnDirectory(applicator)
