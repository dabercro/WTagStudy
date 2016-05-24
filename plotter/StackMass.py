#!/usr/bin/env python

from Stack import *

plotter.SetForceTop('W mass (tt)')
ReadExceptionConfig('mass')

if __name__ == '__main__':
    RunPlots(['mass'])
