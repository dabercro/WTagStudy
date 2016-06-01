# These are just for the users to loop over

categories = ['leading','trailing','mass']
#regions    = ['bwindow','dphilep','topmass','toppruned']
regions    = ['bwindow','dphilep','nsmalljets','topmass','fatjetPt']

# Two dictionaries to define the cuts for separate categories and control regions

# categoryCuts = {
#     'leading' : 'fatjet1Pt > 0',
#     'trailing' : 'fatjet2Pt > 0'
#     }

bwindow = 'fatjet1DRTightB > 0.6 && fatjet1DRTightB < 1.2'
dphilep = 'fatjet1DPhiLep1 > 2.0'
topmass = '(topMass_11 > 120 || topMass_12 > 120)'
toppruned = '(topPrunedM_11 > 70 || topPrunedM_12 > 70)'
nbtags = 'n_bjetsLoose == 2'
semilep = 'n_tightlep == 1'
nsmalljets = '(n_jetsNotFat == 3 && fatjet2Pt < 0)'
fatjetPt = 'fatjet1Pt > 250'

base = ' && '.join([
        'fatjet1Pt > 0 && hasThirdFat == 0',
        semilep,
        ])

regionCuts = {
    'nocut' : '1',
    'bwindow' : bwindow,
    'dphilep' : dphilep,
    'topmass' : topmass,
    'toppruned' : toppruned,
    'nbtags' : nbtags,
    'nsmalljets' : nsmalljets,
    'fatjetPt' : fatjetPt,
    'full' : ' && '.join([
            nsmalljets,
            bwindow,
            dphilep,
            nbtags,
#            topmass,
            fatjetPt,
            ])
    }

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

    if category == 'trailing':
        theCut = theCut.replace('fatjet1','fatjet2').replace('_1','_2')
        
    return theCut
#    return '((' + categoryCuts[category] + ') && (' + regionCuts[region] + '))'

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
