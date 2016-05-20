export CrombieFilesPerJob=10
export CrombieNBatchProcs=1
export CrombieQueue=8nh

export CrombieNLocalProcs=`getconf _NPROCESSORS_ONLN`

export CrombieFileBase=wscale
export CrombieEosDir=/store/user/dabercro
export CrombieRegDir=/Users/dabercro/GradSchool/Summer16/Sample
export CrombieTempDir=/Users/dabercro/GradSchool/Summer16/Temp
export CrombieFullDir=/Users/dabercro/GradSchool/Summer16/Full_TopMass
export CrombieSkimDir=/Users/dabercro/GradSchool/Summer16/Skim_TopMass
export CrombieDirList=

export CrombieSlimmerScript=runSlimmer.py
export CrombieJobScriptList=CrombieJobScriptList.txt
export CrombieCheckerScript=$CROMBIEPATH/scripts/CrombieTreeFinder.py

export CrombieGoodRuns=/Users/dabercro/GradSchool/Winter15/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt
