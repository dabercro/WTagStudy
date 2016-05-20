export CrombieFilesPerJob=10
export CrombieNBatchProcs=1
export CrombieQueue=8nh

export CrombieNLocalProcs=`getconf _NPROCESSORS_ONLN`

export CrombieFileBase=wscale
export CrombieEosDir=/store/user/zdemirag/V0005
#export CrombieEosDir=/store/user/amarini/Nero/v1.4
export CrombieRegDir=/afs/cern.ch/work/d/dabercro/eos/cms$CrombieEosDir
export CrombieTempDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Temp
export CrombieFullDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Full_$CROMBIEDATE
export CrombieSkimDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_$CROMBIEDATE
export CrombieDirList=SingleTops.txt

export CrombieSlimmerScript=runSlimmer.py
export CrombieJobScriptList=CrombieJobScriptList.txt
export CrombieCheckerScript=$CROMBIEPATH/scripts/CrombieTreeFinder.py

export CrombieGoodRuns=/Users/dabercro/GradSchool/Winter15/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt
