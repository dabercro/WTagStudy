#!/bin/bash

fresh=$1

source CrombieSlimmingConfig.sh

if [ "$fresh" = "fresh" ]
then
    rm $CrombieSkimDir/*.root 2> /dev/null
    rm $CrombieSkimDir/*/*.root 2> /dev/null
fi

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet1Pt > 0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir $CrombieFullDir --outdir $CrombieSkimDir --json $CrombieGoodRuns

./applyCorrections.py $CrombieSkimDir

if [ "$fresh" = "fast" ]
then
    exit 0
fi

## Data

hadd -f /afs/cern.ch/work/d/dabercro/public/Summer16/Data/wscale_Data.root $CrombieSkimDir/wscale_Single*.root $CrombieSkimDir/wscale_JetHT.root

CrombieFlatSkimmer  --cut '1' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc 1 --indir /afs/cern.ch/work/d/dabercro/public/Summer16/Data --outdir $CrombieSkimDir --json $CrombieGoodRuns -d

## tt stuff

cp $CrombieSkimDir/wscale_TTJets*.root /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets/.

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1DRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/res --json $CrombieGoodRuns

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1DRGenW > 0.2 && fatjet1DRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/probtop --json $CrombieGoodRuns

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1DRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/nonres --json $CrombieGoodRuns

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet2Pt > 0 && fatjet2DRGenW < 0.2' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/res2 --json $CrombieGoodRuns

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet2Pt > 0 && fatjet2DRGenW > 0.2 && fatjet2DRGenW < 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/probtop2 --json $CrombieGoodRuns

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet2Pt > 0 && fatjet2DRGenW > 1.0' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/nonres2 --json $CrombieGoodRuns

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1PrunedM > 125' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/highmass --json $CrombieGoodRuns

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1PrunedM < 125 && fatjet1PrunedM > 35' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/goodmass --json $CrombieGoodRuns

CrombieFlatSkimmer --cut 'n_looselep == 1 && bjet2Pt > 0 && fatjet1Pt > 0 && fatjet1PrunedM < 35' --tree 'events' --copy 'htotal' --run 'runNum' --lumi 'lumiNum' --freq 100000 --numproc $CrombieNLocalProcs --indir /afs/cern.ch/work/d/dabercro/public/Summer16/TTJets --outdir $CrombieSkimDir/lowmass --json $CrombieGoodRuns

