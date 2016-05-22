#!/bin/bash

CompileCrombieTools PlotStack

./Stack.py &
./StackTrailing.py &
./StackMass.py &

wait
