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

if [ "$(hostname)" = "t3desk003.mit.edu" ]
then
    export CrombieInFilesDir=/scratch/dabercro/WTagStudy/Skim_170117
else
    export CrombieInFilesDir=../../Skim_170117
fi

export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

export CrombieCutsFile=cuts.py
