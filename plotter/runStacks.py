#!/bin/bash

CompileCrombieTools PlotStack

./Stack.py &
# ./StackTrailing.py &
./StackMass.py &

wait

source CrombiePlotterConfig.sh

rename jets\  jets $CrombieOutPlotDir/*
