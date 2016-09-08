# WTagStudy

For each tag in this repository,
you should use the first [CrombieTools](https://codedocs.xyz/dabercro/CrombieTools/)
tag that was created after that date.
I tend to tag CrombieTools when I'm about to break backwards compatibility.

If some of these instructions don't seem complete,
there is plenty more documentation describing my typical [workspace setup](https://codedocs.xyz/dabercro/CrombieTools/workspace.html).

## Installation

```
cd <wherever>
git clone https://github.com/dabercro/CrombieTools.git
cd CrombieTools
git checkout <WhateverIsNeeded>
cd <wherever>
git clone https://github.com/dabercro/WTagStudy.git
```

## Skimming

The analysis depends on the creation of Nero Ntuples.
Good luck finding documentation on that...
[Here's the best pointer I know of.](https://twiki.cern.ch/twiki/bin/viewauth/CMS/NeroSamples)

Make sure that `slimmer/80X.txt` and `slimmer/WScale.txt` points to the
EOS locations and dataset names that you want, respectively.
Then, just create the slimmed files from inside `slimmer` with

```
crombie submitlxbatch
```

After all of the files have been created over LXBATCH and successfully slimmed, run the following:

```
./FlatSkimmer.sh
```

You now have fully skimmed files.

## Plotting

There is a chance that you will need to generate a new PU weight histogram for your luminosity.
You can sort of do that inside the `plotter` directory.

```
./MakeNPVHist.py
```

Then point the `slimmer/applyCorrections.py` file to the new histograms and rerun `slimmer/FlatSkimmer.sh`.
To make stack plots, run the following:

```
./Stack.py
```

To make the Cut and Count scale factor, change the `$CrombieMCConfig` inside `CrombiePlotterConfig.sh` and run:

```
./CutAndCount.py
```

If it complains about a missing branch, you need to add a cross section weight with the following command:

```
./AddXSec.py xsec_v1
```

Replace `xsec_v1` with another name if you're trying to make a different branch name.

That's is, you made a scale factor measurement.
Again, for more details on what's going on, visit the
[CrombieTools](https://codedocs.xyz/dabercro/CrombieTools/) documentation.
