source ../slimmer/CrombieSlimmingConfig.sh

export CrombieMCConfig=MCConfig.txt
#export CrombieMCConfig=MCXSec.txt
#export CrombieMCConfig=MCTT.txt
#export CrombieSignalConfig=SignalConfig.txt
#export CrombieExcept_trailing=MCTrailing.txt
#export CrombieExcept_mass=MCMass.txt
export CrombieLuminosity=816.3
#export CrombieLuminosity=2071.44
#export CrombieInFilesDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_160619
export CrombieInFilesDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_160622_LowLumi
export CrombieOutPlotDir=/afs/cern.ch/user/d/dabercro/www/plots/$CROMBIEDATE\_LowLumi_madgraph
export CrombieOutLimitTreeDir=limits/$CROMBIEDATE

export CrombieCutsFile=cuts.py
