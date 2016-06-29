source ../slimmer/CrombieSlimmingConfig.sh

export CrombieMCConfig=MCConfig.txt
#export CrombieExcept_hadronic=MCTTJets.txt

#export CrombieMCConfig=MCHadronic.txt
export CrombieLuminosity=2596.9
#export CrombieLuminosity=2071.44
export CrombieInFilesDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_160629
export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE

export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

#export CrombieCutsFile=cutsHad.py
export CrombieCutsFile=cuts.py
