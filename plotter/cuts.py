# Used in full region

regions    = ['bwindow','dphilep','nsmalljets']

# Two dictionaries to define the cuts for separate categories and control regions

# categoryCuts = {
#     'leading' : 'fatjet1Pt > 0',
#     'trailing' : 'fatjet2Pt > 0'
#     }

regionCuts = {
    'nocut' : '1',
#    'nocut' : 'vectorSumPt(lep1Pt,lep1Phi,met,metPhi) > 100',
    'semilep' : 'n_tightlep == 1 && n_looselep == 1', # && abs(lep1PdgId) == 13',
    'bwindow' : 'fatjetDRLooseB > 0.8 && fatjetDRLooseB < 1.2',
    'dphilep' : 'fatjetDPhiLep1 > 2.0',
    'topmass' : '(topMass_11 > 120 || topMass_12 > 120)',
    'toppruned' : '(topPrunedM_11 > 70 || topPrunedM_12 > 70)',
    'nbtags' : 'n_bjetsLoose == 2',
    'nsmalljets' : '((n_jetsNotFat == 3 && fatjet2Pt < 0) || (n_jetsNotFat == 2))',
    'fatjetPt' : 'fatjetPt > 100',
    'fullhadronic' : 'fatjet2Pt > 100 && n_looselep == 0',
    'tau21' : 'fatjettau21 < 0.6',
    'massp' : 'fatjetPrunedM > 60 && fatjetPrunedM < 110',
    }

def JoinCuts(toJoin, cuts=regionCuts):
    return ' && '.join([cuts[cut] for cut in toJoin])

base = ' && '.join([
        'fatjetPt > 250 && thirdFatMass < 50',
        JoinCuts([
                'nbtags',
                ]),
        ])

regionCuts['full'] = JoinCuts(regions,regionCuts)

fullhadCuts = {
    'boostedt' : 'fatjet1tau32 < 0.5',
    'ht' : 'jet_ht > 800',
    }

# A weight applied to all MC

defaultMCWeight = 'mcFactors * topPtReweighting'

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

    if category == 'fullhad':
        theCut = theCut.replace('fatjet1','fatjet2').replace('_1','_2')
        theCut = ' && '.join([
                theCut,
                JoinCuts(cuts=fullhadCuts,toJoin=fullhadCuts.keys())
                ])
    else:
        theCut = ' && '.join([
                theCut,
                regionCuts['semilep']
                ])
                
    if category == 'nolowmass':
        theCut += ' && fatjetPrunedM > 25'
        
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
