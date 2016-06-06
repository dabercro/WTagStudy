# These are just for the users to loop over

categories = ['leading','trailing','mass']
regions    = ['bwindow','dphilep','nsmalljets']
#regions    = ['bwindow','nsmalljets','fullhadronic']

# Two dictionaries to define the cuts for separate categories and control regions

# categoryCuts = {
#     'leading' : 'fatjet1Pt > 0',
#     'trailing' : 'fatjet2Pt > 0'
#     }

bwindow = 'fatjet1DRLooseB > 0.8 && fatjet1DRLooseB < 1.2'
dphilep = 'fatjet1DPhiLep1 > 2.0'
topmass = '(topMass_11 > 120 || topMass_12 > 120)'
toppruned = '(topPrunedM_11 > 70 || topPrunedM_12 > 70)'
nbtags = 'n_bjetsLoose == 2'
semilep = 'n_tightlep == 1'
nsmalljets = 'n_jetsNotFat == 3'
fatjetPt = 'fatjet1Pt > 100'
fullhadronic = 'fatjet2Pt > 100 && fatjet2DRMediumB < 1.2 && n_looselep == 0'

tau21 = 'fatjet1tau21 < 0.6'
massp = 'fatjet1PrunedM > 60 && fatjet1PrunedM < 110'

base = ' && '.join([
        'fatjet1Pt > 250 && hasThirdFat == 0',
        semilep,
        nbtags,
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
    'fullhadronic' : fullhadronic,
    'tau21' : tau21,
    'massp' : massp,
    'full' : ' && '.join([
            nsmalljets,
            bwindow,
            dphilep,
#            nbtags,
#            topmass,
#            fatjetPt,
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
