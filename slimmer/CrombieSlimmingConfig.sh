export CrombieFilesPerJob=20
export CrombieNBatchProcs=4
export CrombieQueue=2nw4cores

if [ "$(hostname)" = "dabercro-MacBookAir" ]
then
    export CrombieNLocalProcs=3
else
    export CrombieNLocalProcs=6
fi

export CrombieEosDir=80X.txt
export CrombieFileBase=wscale
export CrombieRegDir=/afs/cern.ch/work/d/dabercro/eosuser/user/d/dabercro/80X
#export CrombieFullDir=/tmp/dabercro/Full_$CROMBIEDATE
export CrombieTempDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Temp
export CrombieFullDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Full_160713
export CrombieSkimDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_$CROMBIEDATE
export CrombieDirList=WScale.txt

export CrombieSlimmerScript=runSlimmer.py
export CrombieJobScriptList=JobScriptList.txt
export CrombieCheckerScript=$CROMBIEPATH/scripts/CrombieTreeFinder.py

#export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-273730_13TeV_PromptReco_Collisions16_JSON.txt
#export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274240_13TeV_PromptReco_Collisions16_JSON.txt
#export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274421_13TeV_PromptReco_Collisions16_JSON.txt
#export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274443_13TeV_PromptReco_Collisions16_JSON.txt
#export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt
#export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt
export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276097_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt
