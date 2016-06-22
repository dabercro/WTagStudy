source ../slimmer/CrombieSlimmingConfig.sh

export CrombieMCConfig=MCConfig.txt
#export CrombieMCConfig=MCTT.txt
#export CrombieMCConfig=MCTest.txt
#export CrombieSignalConfig=SignalConfig.txt
#export CrombieLuminosity=2071.44
export CrombieLuminosity=814.56
export CrombieInFilesDir=../../Skim_LowLumi
export CrombieOutPlotDir=plots/$CROMBIEDATE\_LowLumi_both
export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

export CrombieCutsFile=cuts.py
