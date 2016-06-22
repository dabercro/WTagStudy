#!/bin/bash

rm *.pdf 2> /dev/null

files="semilep_full_fatjetPrunedM.pdf semilep_full_fatjetPrunedMuncorr.pdf semilep_full_fatjettau21.pdf semilep_nocut_fatjetDPhiLep1.pdf semilep_nocut_fatjetDRGenW.pdf semilep_nocut_fatjetDRLooseB.pdf"

for f in $files
do
    wget http://dabercro.web.cern.ch/dabercro/plots/160622_fin/$f
    pdfcrop $f $f
done
