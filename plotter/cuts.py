# These are just for the users to loop over

categories = ['leading','trailing','mass']
regions    = ['bwindow','dphilep','topmass','toppruned']

# Two dictionaries to define the cuts for separate categories and control regions

# categoryCuts = {
#     'leading' : 'fatjet1Pt > 0',
#     'trailing' : 'fatjet2Pt > 0'
#     }

base = 'fatjet1Pt > 0'
bwindow = 'fatjet1DRTightB > 0.7 && fatjet1DRTightB < 1.5'
dphilep = 'fatjet1DPhiLep1 > 2.0'
topmass = 'topMass_11 > 120 && topMass_12 > 120'
toppruned = 'topPrunedM_11 > 100 && topPrunedM_21 > 100'

regionCuts = {
    'nocut' : '1',
    'bwindow' : bwindow,
    'dphilep' : dphilep,
    'topmass' : topmass,
    'toppruned' : toppruned
    }

# A weight applied to all MC

defaultMCWeight = 'mcWeight'

# Additional weights applied to certain control regions

additions    = { # key : [Data,MC]
    'default' : ['0',defaultMCWeight]
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
