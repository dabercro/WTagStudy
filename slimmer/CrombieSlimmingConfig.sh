export CrombieFilesPerJob=60
export CrombieQueue=8nh

if [ "$(hostname)" = "dabercro-MacBookAir" ]
then
    export CrombieNLocalProcs=2
else
    export CrombieNLocalProcs=12
fi

export CrombieEosDir=/store/group/phys_higgs/ceballos/setup80x_ichep/Data/Nero/v2.0/
export CrombieFileBase=wscale
export CrombieRegDir=/afs/cern.ch/work/d/dabercro/eosuser/user/d/dabercro/80X
#export CrombieFullDir=/tmp/dabercro/Full_$CROMBIEDATE
export CrombieTempDir=/afs/cern.ch/work/d/dabercro/public/Fall16/Temp
export CrombieFullDir=/afs/cern.ch/work/d/dabercro/public/Fall16/Full_160726
export CrombieSkimDir=/afs/cern.ch/work/d/dabercro/public/Fall16/Skim_$(CROMBIEDATE)
export CrombieDirList=Data.txt

export CrombieSlimmerScript=runSlimmer.py
export CrombieJobScriptList=JobScriptList.txt
export CrombieCheckerScript=$CROMBIEPATH/scripts/findtree.py

export CrombieGoodRuns=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
