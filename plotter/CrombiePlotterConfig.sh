source ../slimmer/CrombieSlimmingConfig.sh

#export CrombieMCConfig=MCLongName.txt
export CrombieMCConfig=MCBackground.txt
#export CrombieMCConfig=MCTruthMatch.txt
#export CrombieMCConfig=MCConfig.txt
#export CrombieExcept_hadronic=MCTTJets.txt

#export CrombieMCConfig=MCHadronic.txt
export CrombieLuminosity=2596.9
#export CrombieLuminosity=2071.44
export CrombieInFilesDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_160704
export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE\_check

export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

#export CrombieCutsFile=cutsHad.py
export CrombieCutsFile=cuts.py
#export CrombieCutsFile=cutsNew.py
