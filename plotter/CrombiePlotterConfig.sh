source ../slimmer/CrombieSlimmingConfig.sh

#export CrombieMCConfig=MCBackground.txt
export CrombieMCConfig=MCTruthMatch.txt
#export CrombieMCConfig=MCHadronic.txt

#export CrombieMCConfig=MCHadronic.txt
export CrombieLuminosity=6264.6
export CrombieInFilesDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_160714
export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE

export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

#export CrombieCutsFile=cutsHad.py
export CrombieCutsFile=cuts.py
#export CrombieCutsFile=cutsNew.py
