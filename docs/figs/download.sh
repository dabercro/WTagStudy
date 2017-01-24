#!/bin/bash

crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160714/semilep_nocut_fatjetDRLooseB,160714/semilep_nocut_fatjetDPhiLep1,160714/semilep_nocut_fatjetDRGenW,160714/semilep_full_ntau_mediumB_n_jetsTot,160714/semilep_full_ntau_mediumB_ntot_fatjetPrunedML2L3,160714/semilep_full_ntau_mediumB_ntot_fatjettau21,160714/semilep_full_ntau_mediumB_ntot_massp_tau21_fatjetPrunedML2L3,160714/semilep_full_ntau_mediumB_ntot_massp_tau21_fatjettau21" 

test "$(hostname)" = "dabercro-MacBookAir" && flag=" -s" || flag=""
rename$flag 0. 0_ */*0.*

for f in */*.pdf
do
    pdfcrop $f $f
done
