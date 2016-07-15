#export CrombieMCConfig=MCTruthMatch.txt
export CrombieMCConfig=MCBackground.txt
export CrombieExcept_herwig=MCBackgroundHerwig.txt
export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE

source ../slimmer/CrombieSlimmingConfig.sh
#export CrombieMCConfig=MCHadronic.txt

#export CrombieMCConfig=MCHadronic.txt
export CrombieLuminosity=7647.6
export CrombieInFilesDir=../../Skim_160714

export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

#export CrombieCutsFile=cutsHad.py
export CrombieCutsFile=cuts.py
#export CrombieCutsFile=cutsNew.py
