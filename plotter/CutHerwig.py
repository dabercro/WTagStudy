#!/usr/bin/env python

from CutAndCount import *

if __name__ == "__main__":
    histAnalysis.ReadMCConfig(os.environ['CrombieExcept_herwig'])
    main()
