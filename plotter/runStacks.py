#!/bin/bash

CompileCrombieTools PlotStack

source CrombiePlotterConfig.sh

mkdir -p $CrombieOutPlotDir 2> /dev/null

./Stack.py &
#./StackTrailing.py &

wait

cd ~/www
makePage.sh $CrombieOutPlotDir 3
cd - 1> /dev/null
