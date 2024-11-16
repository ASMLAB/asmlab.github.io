---
title: "ocean"
categories: ["modeling","MITgcm"]
tags: ["modeling"]
description: ""
weight: 3
---

There is a verification called `global_ocean.cs32x15` that uses the same grid as `aim.5l_cs`.
So, let's get used to it before trying the atmosphere-ocean coupled model.

{{< toc >}}

## description of this experiment
The description of this example is provided in the `README` file.
{{< hint type=note icon=gdoc_check title=global_ocean.cs32x15 >}}
global ocean using the cubed-sphere grid 32x32x32 with 15 levels

=================================================================

Specific option:
* Use Non-Linear Free surface formulation with z* coordinate
   with real fresh-water flux.
* Oceanic set-up on the cubed-sphere grid using the vector-invariant
   formulation.

Forcing :
 use Monthly mean climatological forcing (except P-E-R, annual mean).
 same data set as global-ocean lat-long experiments but interpolated
  on CS-32 grid.

Comments:
* bathymetry :
 designed to be coupled to Atmospheric model, therefore includes
 most of the semi-enclosed sea (Mediterranean, Black-Sea, Red-Sea,
   Hudson Bay ...)
 bathy_cs32.bin: initial bathymetry
   h < 0 is meant to stay wet-point whatever delZ(1) is ; Consequently
   the global ocean area is not affected by the vertical resolution.
 bathy_Hmin50.bin: bathymetry file used in the current set-up
    generated from bathy_cs32.bin using matlab script mk_bathy4gcm.m
 mk_bathy4gcm.m matlab script that deepen all shallow point up to 50m.
* global integral of E-P-R and annual mean net Q flux are zero.
* package thSIce and bulk_forc are included but not used in the standard
  set-up.

* additional forcing fields and parameter files are provided (in input.thsice)
  in order to illustrate the use of thSIce pkg.
  the output of a short run (20.iter) is given in results/output_thsice.txt

October 1rst, 2005:
* input.viscA4/data has been added to test biharmonic viscosity on CS-grid
  with side-drag. However, this set of parameters has only be used for
  short tests and is not recommended to begin with.
{{< /hint >}}


## compile
It is similar to what we did for the atmospheric model. 
First, open the terminal and go to the example directory
`cd /MITgcm/verification/global_ocean.cs32x15`

We also want to use more than 1 cpu, we use `SIZE.h_mpi`.
- go to `code` directory
- rename `SIZE.h` as `SIZE.h_single`
- rename `SIZE.h_mpi` as `SIZE.h` {{< katex >}}\rightarrow{{< /katex >}} It specifies the number of cpus as 4.
- go to `build` directory
- do `../../../tools/genmake2 -mods ../code -optfile ../../../tools/build_options/darwin_amd64_gfortran -mpi`
- if it is finished without a severe error, do `make depend`
- if it is finished without a severe error, do `make`
- if you have `mitgcmuv`, then the compliation is successful

## preparation
We first try to run the model with the default setting.
- go to `run` directory
- copy all input files to here: `cp ../input/* .`
- create a sympolic link of the input files to here: `./prepare_run`
- create a sympolic link of the executable file to here: `ln -s ../build/mitgcmuv .`
<!-- - overwrite the [`data`](/mitgcmfiles/atmos/data) file to here -->

## model integration
Now, let's run the model!
- execute the run: `mpirun -np 4 ./mitgcmuv`

## analysis

## additional experiments
### adding age tracer
We can measure the age of the water mass. The age represents how long it has passed since a particular water mass was at the surface. This shows the ocean circulation: you may find "young" water mass at depth where there is sinking and "old" water mass where there is upwelling.

To do this, we need to activate `ptracers` package that allows us to add passive tracers in the simulation.
- go to `code` directory: `cd code_age`
- add a line in `packages.conf` file: `echo 'ptracers' >> packages.conf`
- copy a couple of files that compute the age of water mass: `cp ../../tutorial_global_oce_latlon/code/ptracers_* .`
- then, let's compile the code in the build directory: 
    - go to `build` directory
    - do `make CLEAN`
    - compile the code again as in [compile](/research/MITgcm/ocean/#compile)
- go to the `run` directory
- copy an input parameter file for a tracers: `cp ../../tutorial_global_oce_latlon/input/data.ptracers .`
- activate `ptracer` package: add ` usePTRACERS=.TRUE.,` in `data.pkg`
- we need to tell the model that the initial time step for tracer is 72000: add ` PTRACERS_Iter0=72000,` in `data.ptracers`
- run the model as in [model integration](/research/MITgcm/ocean/#model-integration)


### simulation with sea-ice package
This example provides a couple of variations from the default setting. 
So, let's try the one with sea ice using the settingin `input.seaice`.
- create the run directory: `mkdir run.seaice`
- go to this directory: `cd run.seaice`
- copy all input files to here: `cp ../input/* .`
- create a sympolic link of the input files to here: `./prepare_run`
- Then, overwrite some of the input files with those related to sea ice experiment: `cp ../input.seaice/* .`
- create a sympolic link of the input files associated with this sea ice experiment: `./prepare_run`
- create a sympolic link of the executable file to here: `ln -s ../build/mitgcmuv .`
- run the model as in [model integration](/research/MITgcm/ocean/#model-integration)
