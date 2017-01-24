#!/bin/bash



test "$(hostname)" = "dabercro-MacBookAir" && flag=" -s" || flag=""
rename$flag 0. 0_ */*0.*

for f in */*.pdf
do
    pdfcrop $f $f
done
