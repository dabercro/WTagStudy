export CrombieMCConfig=MCBackground.txt
export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE\_background
#export CrombieMCConfig=MCTruthMatch.txt
#export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE

source ../slimmer/CrombieSlimmingConfig.sh
#export CrombieMCConfig=MCHadronic.txt

#export CrombieMCConfig=MCHadronic.txt
export CrombieLuminosity=7647.6
export CrombieInFilesDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_160714

export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

#export CrombieCutsFile=cutsHad.py
export CrombieCutsFile=cuts.py
#export CrombieCutsFile=cutsNew.py
