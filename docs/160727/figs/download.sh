#!/bin/bash

rm */*.pdf
rmdir 160*

crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160725_nowln/semilep_full_fatjetPrunedML2L3" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160725/semilep_full_fatjetPrunedML2L3,160725_background/semilep_full_fatjetPrunedML2L3,160725_midbackground/semilep_full_fatjetPrunedML2L3,160725_morebackground/semilep_full_fatjetPrunedML2L3" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160725/semilep_full_massp_tau21_fatjettau21,160725_background/semilep_full_massp_tau21_fatjettau21,160725_midbackground/semilep_full_massp_tau21_fatjettau21,160725_morebackground/semilep_full_massp_tau21_fatjettau21,160725/semilep_full_fatjettau21,160725_background/semilep_full_fatjettau21,160725_midbackground/semilep_full_fatjettau21,160725_morebackground/semilep_full_fatjettau21,160725/semilep_full_massp_tau21_fatjetPrunedML2L3,160725_background/semilep_full_massp_tau21_fatjetPrunedML2L3,160725_midbackground/semilep_full_massp_tau21_fatjetPrunedML2L3,160725_morebackground/semilep_full_massp_tau21_fatjetPrunedML2L3,160725/semilep_full_fatjetPrunedML2L3,160725_background/semilep_full_fatjetPrunedML2L3,160725_midbackground/semilep_full_fatjetPrunedML2L3,160725_morebackground/semilep_full_fatjetPrunedML2L3" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160725/semilep_full_massp_tau21_fatjettau21,160725/semilep_full_fatjettau21,160725/semilep_full_highpt_fatjettau21,160725/semilep_full_massp_tau21_fatjetDPhiLep1,160725/semilep_full_fatjetDPhiLep1,160725/semilep_full_highpt_fatjetDPhiLep1,160725/semilep_full_massp_tau21_fatjetPrunedML2L3,160725/semilep_full_fatjetPrunedML2L3,160725/semilep_full_highpt_fatjetPrunedML2L3,160725/semilep_full_massp_tau21_fatjetDRLooseB,160725/semilep_full_fatjetDRLooseB,160725/semilep_full_highpt_fatjetDRLooseB,160725/semilep_full_massp_tau21_n_bjetsLoose,160725/semilep_full_n_bjetsLoose,160725/semilep_full_highpt_n_bjetsLoose,160725/semilep_full_massp_tau21_n_bjetsMedium,160725/semilep_full_n_bjetsMedium,160725/semilep_full_highpt_n_bjetsMedium,160725/semilep_full_massp_tau21_fatjetMass,160725/semilep_full_fatjetMass,160725/semilep_full_highpt_fatjetMass,160725/semilep_full_massp_tau21_fatjetPt,160725/semilep_full_fatjetPt,160725/semilep_full_highpt_fatjetPt,160725/semilep_full_massp_tau21_n_jetsNotFat,160725/semilep_full_n_jetsNotFat,160725/semilep_full_highpt_n_jetsNotFat,160725/semilep_full_massp_tau21_n_bjetsTight,160725/semilep_full_n_bjetsTight,160725/semilep_full_highpt_n_bjetsTight,160725/semilep_full_massp_tau21_n_jetsTot,160725/semilep_full_n_jetsTot,160725/semilep_full_highpt_n_jetsTot" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160719/fatjetPrunedMx" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160707/WPt_comparison" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160725/semilep_nocut_n_bjetsMedium,160725/semilep_nocut_n_jetsNotFat,160725/semilep_nocut_n_jetsTot" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160725/semilep_full_0.0_fatjetPrunedML2L3,160725/semilep_full_0.1_fatjetPrunedML2L3,160725/semilep_full_0.2_fatjetPrunedML2L3,160725/semilep_full_0.3_fatjetPrunedML2L3,160725/semilep_full_0.4_fatjetPrunedML2L3,160725/semilep_full_0.5_fatjetPrunedML2L3,160725/semilep_full_0.6_fatjetPrunedML2L3,160725/semilep_full_0.7_fatjetPrunedML2L3" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160725/semilep_nocut_nsmalljets_fatjetDPhiLep1,160725/semilep_nocut_nsmalljets_fatjetDRLooseB" 
crombie downloadtar "http://dabercro.web.cern.ch/dabercro/plotviewer/viewplot/static/viewplot/returntar.php?only=pdf&files=160725/semilep_nocut_nsmalljets_fatjetPrunedML2L3" 

rm */*n_bjetsLoose.pdf
rm */*highpt*Pt.pdf

mv 160707/WPt_comparison.pdf 160707/WPt_comparisonx.pdf
rename -s 0. 0_ */*0.*
