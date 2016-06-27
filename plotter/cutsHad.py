# Used in full region

regions = ['bwindow','ht','jetmasses','jetdphimet']

# Two dictionaries to define the cuts for separate categories and control regions

regionCuts = {
    'jetdphimet' : 'fatjet1DPhiMet > 1.0',
    'topnsub' : 'fatjet1tau21 < 0.6',
    'jetmasses' : 'fatjet1PrunedM > 60 && topMass_11 < 280',
    'moarpt' : 'fatjet2Pt > 250',
    'nocut' : '1',
    'nolep' : 'n_looselep == 0',
    'nopho' : 'n_loosepho == 0',
    'boostedt' : 'fatjet1tau32 < 0.5',
    'ht' : 'jet_ht > 800',
    'bwindow' : 'fatjet2DRMediumB > 0.8 && fatjet2DRMediumB < 1.2 && fatjet1DRMediumB < 1.2',
    'subjettags' : 'fatjet1MaxBTag > 0.8 && fatjet2MaxBTag < 0.6',
    'topmass' : '(topMass_11 > 120 || topMass_12 > 120)',
    'toppruned' : '(topPrunedM_11 > 70 || topPrunedM_12 > 70)',
    'nbtags' : 'n_bjetsMedium == 2 && n_bjetsLoose == 2 && n_bjetsTight > 0',
    'nsmalljets' : 'n_jetsNotFat < 3',
    'fatjetPt' : 'fatjetPt > 100',
    'fullhadronic' : 'fatjet2Pt > 100 && n_looselep == 0',
    'tau21' : 'fatjettau21 < 0.6',
    'massp' : 'fatjetPrunedM > 60 && fatjetPrunedM < 110',
    'met' : 'met < 100',
    'njetstop' : 'n_jetsTot > 5',
    }

def JoinCuts(toJoin, cuts=regionCuts):
    return ' && '.join([cuts[cut] for cut in toJoin])

base = ' && '.join([
        'fatjet1Pt > 300',
        JoinCuts([
                'nbtags',
                'nolep',
                'nopho',
                'njetstop',
                ]),
        ])

regionCuts['full'] = JoinCuts(regions,regionCuts)

# A weight applied to all MC

defaultMCWeight = 'mcFactors'

# Additional weights applied to certain control regions

additions    = { # key : [Data,MC]
    'default' : ['1',defaultMCWeight]
    }

# Do not change the names of these functions or required parameters
# Otherwise you cannot use some convenience functions
# Generally you can probably leave these alone

def cut(category,inRegions):
    theCuts = [base]
    for region in inRegions.split('_'):
        theCuts.append(regionCuts[region])

    theCut = ' && '.join(theCuts)

    return theCut


def dataMCCuts(region, isData):
    key = 'default'
    if additions.get(region):
        key = region

    index = 1
    if isData:
        index = 0

    if key == 'default' or index == 0:
        return '(' + additions[key][index] + ')'
    else:
        return '((' + additions[key][index] + ')*(' + defaultMCWeight + '))'
