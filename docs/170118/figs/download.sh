#!/bin/bash

crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=170118/semilep_full_fatjettau21,170118/semilep_nocut_nsmalljets_fatjetDPhiLep1,170118/semilep_full_fatjetPrunedML2L3,170118/semilep_nocut_nsmalljets_fatjetPrunedML2L3,170118/semilep_nocut_nsmalljets_fatjetDRLooseB"
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=170118/semilep_full_0.0_fatjetPrunedML2L3,170118/semilep_full_0.1_fatjetPrunedML2L3,170118/semilep_full_massp_tau21_fatjetPrunedML2L3,170118/semilep_full_0.2_fatjetPrunedML2L3,170118/semilep_full_0.3_fatjetPrunedML2L3,170118/semilep_full_0.4_fatjetPrunedML2L3,170118/semilep_full_0.5_fatjetPrunedML2L3,170118/semilep_full_0.6_fatjetPrunedML2L3,170118/semilep_full_0.7_fatjetPrunedML2L3,170118/semilep_full_fatjetPrunedML2L3,170118/semilep_full_highpt_fatjetPrunedML2L3"
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=170118_background/semilep_full_0.3_fatjetPrunedML2L3,170118_background/semilep_full_0.5_fatjetPrunedML2L3,170118_background/semilep_full_fatjetPrunedML2L3,170118_background/smearedup_mass"
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=170118_morebackground/semilep_full_fatjetPrunedML2L3,170118_up/semilep_full_fatjetPrunedML2L3"
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=170118/semilep_full_massp_tau21_fatjettau21"

test "$(hostname)" = "dabercro-MacBookAir" && flag=" -s" || flag=""
rename$flag 0. 0_ */*0.*

for f in */*.pdf
do
    pdfcrop $f $f
done
