source ../slimmer/CrombieSlimmingConfig.sh

#export CrombieMCConfig=MCConfig.txt
#export CrombieExcept_hadronic=MCTTJets.txt
export CrombieMCConfig=MCHadronic.txt
export CrombieLuminosity=2550.0
export CrombieInFilesDir=/Users/dabercro/GradSchool/Summer16/Skim_160627
export CrombieOutPlotDir=plots/$CROMBIEDATE
export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

export CrombieCutsFile=cutsHad.py
