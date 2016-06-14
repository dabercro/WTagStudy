export CrombieFilesPerJob=8
export CrombieNBatchProcs=1
export CrombieQueue=8nh

export CrombieNLocalProcs=6

export CrombieEosDir=80X.txt

export CrombieFileBase=wscale
#export CrombieEosDir=/store/user/zdemirag/setup80x/Nero/zey_base
#export CrombieRegDir=/afs/cern.ch/work/d/dabercro/eoscms/cms$CrombieEosDir
export CrombieTempDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Temp_$CROMBIEDATE
export CrombieFullDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Full_$CROMBIEDATE
export CrombieSkimDir=/afs/cern.ch/work/d/dabercro/public/Summer16/Skim_$CROMBIEDATE
#export CrombieDirList=TTJets.txt

export CrombieSlimmerScript=runSlimmer.py
export CrombieJobScriptList=CrombieJobScriptList.txt
export CrombieCheckerScript=$CROMBIEPATH/scripts/CrombieTreeFinder.py

export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274240_13TeV_PromptReco_Collisions16_JSON.txt
