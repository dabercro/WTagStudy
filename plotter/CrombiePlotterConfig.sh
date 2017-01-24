export CrombieMCConfig=MCTruthMatch.txt
#export CrombieMCConfig=MCBackground.txt
#export CrombieMCConfig=MCBackground_mid.txt
export CrombieExcept_herwig=MCBackgroundHerwig.txt

if [ "$(hostname)" = "dabercro-MacBookAir" ]
then
    export CrombieOutPlotDir=plots/$CROMBIEDATE
else    
    export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE
fi

source ../slimmer/CrombieSlimmingConfig.sh

export CrombieLuminosity=34100.0

skimdir=Skim_170120

if [ "$(hostname)" = "t3desk003.mit.edu" ]
then
    export CrombieInFilesDir=/scratch/dabercro/flatTrees/WTagStudy/$skimdir
else
    export CrombieInFilesDir=../../$skimdir
fi

export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

export CrombieCutsFile=cuts.py
