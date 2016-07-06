#!/bin/bash

dirs="old new small powheg herwig"
images="semilep_full_fatjetPrunedM.pdf semilep_full_fatjettau21.pdf"

for dir in $dirs
do

    if [ ! -d $dir ]
    then
        mkdir $dir
    fi

    url=http://dabercro.web.cern.ch/dabercro/plots/16070
    if [ "$dir" = "small" ]
    then
        url=$url\5/
    else
        url=$url\4_$dir/
    fi

    for image in $images
    do
        echo $url$image
        wget $url$image
        mv $image $dir/$image
    done

done