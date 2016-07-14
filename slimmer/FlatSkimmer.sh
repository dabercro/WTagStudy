#!/bin/bash

fresh=$1

source CrombieSlimmingConfig.sh

if [ "$fresh" = "fresh" ]
then
    rm $CrombieSkimDir/*.root 2> /dev/null
    rm $CrombieSkimDir/*/*.root 2> /dev/null
fi

CrombieFlatSkimmer --cut 'fatjet1Pt > 200 && bjet2Pt > 0 && n_jetsNotFat < 5 && n_tightlep == 1 && n_looselep == 1' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir $CrombieFullDir --outdir $CrombieSkimDir --json $CrombieGoodRuns

./applyCorrections.py $CrombieSkimDir

if [ "$fresh" = "fast" ]
then
    exit 0
fi

rm /afs/cern.ch/work/d/dabercro/public/Summer16/Data/* /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/*

## Data

hadd -f /afs/cern.ch/work/d/dabercro/public/Summer16/Data/wscale_Data.root $CrombieSkimDir/wscale_Single*.root # $CrombieSkimDir/wscale_JetHT.root $CrombieSkimDir/wscale_MET.root

CrombieFlatSkimmer  --cut '1' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc 1 --indir /afs/cern.ch/work/d/dabercro/public/Summer16/Data --outdir $CrombieSkimDir --json $CrombieGoodRuns -d

## tt stuff

mv $CrombieSkimDir/wscale_TT*.root /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/.
mv /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/*DiLept* $CrombieSkimDir/.
mv /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/*TTJets_HT-* $CrombieSkimDir/.

CrombieFlatSkimmer --cut 'fatjetDRWq1 < 0.8 && fatjetDRGenB > 0.8' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/WMerged --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjetDRWq1 < 0.8 && fatjetDRGenB < 0.8' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/TopMerged --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjetDRWq1 > 0.8 && fatjetDRWq2 < 0.8 && fatjetDRGenB < 0.8' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/BQuark --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjetDRWq1 > 0.8 && fatjetDRWq2 < 0.8 && fatjetDRGenB > 0.8' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/Quark --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjetDRWq1 > 0.8 && fatjetDRWq2 > 0.8 && fatjetDRGenB < 0.8' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/B --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjetDRWq1 > 0.8 && fatjetDRWq2 > 0.8 && fatjetDRGenB > 0.8' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/Recoiling --json $CrombieGoodRuns -d

#CrombieFlatSkimmer --cut 'fatjet1DRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/res --json $CrombieGoodRuns -d

#CrombieFlatSkimmer --cut 'fatjet1DRGenW > 0.2 && fatjet1DRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/probtop --json $CrombieGoodRuns -d

#CrombieFlatSkimmer --cut 'fatjet1DRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/nonres --json $CrombieGoodRuns -d

#rm /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/*SingleLept*
#mv $CrombieSkimDir/wscale_TTJets_HT-*.root /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/.

#CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/res2 --json $CrombieGoodRuns -d

#CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW > 0.2 && fatjet2DRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/probtop2 --json $CrombieGoodRuns -d

#CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/nonres2 --json $CrombieGoodRuns -d

rm /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/*
