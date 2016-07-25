#export CrombieMCConfig=MCTruthMatch.txt
export CrombieMCConfig=MCBackground.txt
#export CrombieMCConfig=MCBackground_mid.txt
export CrombieExcept_herwig=MCBackgroundHerwig.txt

if [ "$(hostname)" = "dabercro-MacBookAir" ]
then
    export CrombieOutPlotDir=plots/$CROMBIEDATE
else    
    export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE
fi

source ../slimmer/CrombieSlimmingConfig.sh

#export CrombieLuminosity=7647.6
export CrombieLuminosity=12918.14
export CrombieInFilesDir=../../Skim_160722

export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

export CrombieCutsFile=cuts.py
