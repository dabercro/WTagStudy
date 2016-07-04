#!/bin/bash

fresh=$1

source CrombieSlimmingConfig.sh

if [ "$fresh" = "fresh" ]
then
    rm $CrombieSkimDir/*.root 2> /dev/null
    rm $CrombieSkimDir/*/*.root 2> /dev/null
    rm /afs/cern.ch/work/d/dabercro/public/Summer16/Data/* /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/*
fi

CrombieFlatSkimmer --cut 'fatjet1Pt > 200 && bjet2Pt > 0 && n_looselep < 2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir $CrombieFullDir --outdir $CrombieSkimDir --json $CrombieGoodRuns

./applyCorrections.py $CrombieSkimDir

if [ "$fresh" = "fast" ]
then
    exit 0
fi

## Data

hadd -f /afs/cern.ch/work/d/dabercro/public/Summer16/Data/wscale_Data.root $CrombieSkimDir/wscale_Single*.root $CrombieSkimDir/wscale_JetHT.root $CrombieSkimDir/wscale_MET.root

CrombieFlatSkimmer  --cut '1' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc 1 --indir /afs/cern.ch/work/d/dabercro/public/Summer16/Data --outdir $CrombieSkimDir --json $CrombieGoodRuns -d

mv /afs/cern.ch/work/d/dabercro/public/Summer16/Data/wscale_Data.root /afs/cern.ch/work/d/dabercro/public/Summer16/Data/wscale_SmallData.root

CrombieFlatSkimmer  --cut '1' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc 1 --indir /afs/cern.ch/work/d/dabercro/public/Summer16/Data --outdir $CrombieSkimDir --json /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274421_13TeV_PromptReco_Collisions16_JSON.txt -d

## tt stuff

mv $CrombieSkimDir/wscale_TT*.root /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/.
mv /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/*DiLept*.root $CrombieSkimDir/.

CrombieFlatSkimmer --cut 'fatjetDRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/res --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjetDRGenW > 0.2 && fatjetDRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/probtop --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjetDRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/nonres --json $CrombieGoodRuns -d

#CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/res2 --json $CrombieGoodRuns -d

#CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW > 0.2 && fatjet2DRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/probtop2 --json $CrombieGoodRuns -d

#CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/nonres2 --json $CrombieGoodRuns -d
