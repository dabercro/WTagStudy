#!/bin/bash

fresh=$1

source CrombieSlimmingConfig.sh

if [ "$fresh" = "fresh" ]
then
    rm $CrombieSkimDir/*.root 2> /dev/null
    rm $CrombieSkimDir/*/*.root 2> /dev/null
fi

CrombieFlatSkimmer --cut 'n_looselep < 2 && bjet2Pt > 0 && fatjet1Pt > 0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir $CrombieFullDir --outdir $CrombieSkimDir --json $CrombieGoodRuns

mkdir $CrombieSkimDir/wln
mv $CrombieSkimDir/wscale_WJetsToLNu_Pt* $CrombieSkimDir/wln/.

./applyCorrections.py $CrombieSkimDir
./applyCorrectionsW.py $CrombieSkimDir/wln

mv $CrombieSkimDir/wln/* $CrombieSkimDir/.
rmdir $CrombieSkimDir/wln

if [ "$fresh" = "fast" ]
then
    exit 0
fi

rm /afs/cern.ch/work/d/dabercro/public/Summer16/Data/* /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/*

## Data

hadd -f /afs/cern.ch/work/d/dabercro/public/Summer16/Data/wscale_Data.root $CrombieSkimDir/wscale_Single*.root $CrombieSkimDir/wscale_JetHT.root $CrombieSkimDir/wscale_MET.root

CrombieFlatSkimmer  --cut '1' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc 1 --indir /afs/cern.ch/work/d/dabercro/public/Summer16/Data --outdir $CrombieSkimDir --json $CrombieGoodRuns -d

## tt stuff

cp $CrombieSkimDir/wscale_TTJets*.root /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X/.

CrombieFlatSkimmer --cut 'bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1DRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/res --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1DRGenW > 0.2 && fatjet1DRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/probtop --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1DRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/nonres --json $CrombieGoodRuns -d
