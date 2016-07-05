#!/bin/bash

CompileCrombieTools PlotStack

source CrombiePlotterConfig.sh

mkdir -p $CrombieOutPlotDir 2> /dev/null

./StackHadronic.py

plots/makePage.sh $CrombieOutPlotDir 3
