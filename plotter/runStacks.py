#!/bin/bash

CompileCrombieTools PlotStack

source CrombiePlotterConfig.sh

mkdir -p $CrombieOutPlotDir 2> /dev/null

./Stack.py

plots/makePage.sh $CrombieOutPlotDir 3
