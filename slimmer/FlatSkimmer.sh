#!/bin/bash

fresh=$1

source CrombieSlimmingConfig.sh

if [ "$fresh" = "fresh" ]
then
    rm $CrombieSkimDir/*.root 2> /dev/null
    rm $CrombieSkimDir/*/*.root 2> /dev/null
fi

CrombieFlatSkimmer --cut 'fatjet1Pt > 200 && bjet2Pt > 0 && n_jetsNotFat < 5 && ((fatjet2Pt > 200 && n_jetsTot > 4 && n_looselep == 0) || (n_mediumlep == 1 && n_looselep == 1))' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir $CrombieFullDir --outdir $CrombieSkimDir --json $CrombieGoodRuns

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

rm /Users/dabercro/GradSchool/Summer16/Data/* /Users/dabercro/GradSchool/Summer16/TT_80X/*

## Data

hadd -f /Users/dabercro/GradSchool/Summer16/Data/wscale_Data.root $CrombieSkimDir/wscale_Single*.root $CrombieSkimDir/wscale_JetHT.root $CrombieSkimDir/wscale_MET.root

CrombieFlatSkimmer  --cut '1' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc 1 --indir /Users/dabercro/GradSchool/Summer16/Data --outdir $CrombieSkimDir --json $CrombieGoodRuns -d

## tt stuff

cp $CrombieSkimDir/wscale_TTJets*.root /Users/dabercro/GradSchool/Summer16/TT_80X/.

CrombieFlatSkimmer --cut 'fatjet1DRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/res --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjet1DRGenW > 0.2 && fatjet1DRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/probtop --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjet1DRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/nonres --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/res2 --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW > 0.2 && fatjet2DRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/probtop2 --json $CrombieGoodRuns -d

CrombieFlatSkimmer --cut 'fatjet2Pt > 0 && fatjet2DRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TT_80X --outdir $CrombieSkimDir/nonres2 --json $CrombieGoodRuns -d
