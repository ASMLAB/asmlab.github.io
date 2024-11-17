---
title: "atmosphere"
categories: ["modeling","MITgcm"]
tags: ["modeling"]
description: ""
weight: 2
---

MITgcm includes an atmospheric physics as a package and it is in `aim_v23`.
The following is the description of this package you can find in `MITgcm/pkg/aim_v23`.

{{< hint type=note icon=gdoc_check title=aim_v23_description.tex >}}
Package `aim_v23` contains code for an intermediate complexity atmospheric 
physics scheme derived from the physics in the SPEEDY model of Franco Molteni. 
The package contains the SPEEDY physics routines, re-cast to work with pressure
coordinate dynamics, together with code that interfaces the SPEEDY
internal arrays to the MITgcm dynamical kernel.
{{< /hint >}}

The following is the description of the verification named `aim.5l_cs` in [MITgcm's user manual](https://mitgcm.readthedocs.io/en/latest/examples/examples.html#additional-example-experiments-forward-model-setups).

{{< hint type=note icon=gdoc_check title=aim.5l_cs >}}
5-level intermediate atmospheric physics, global configuration on cube sphere grid (32x32 grid points per face, roughly 2.8&deg; resolution). Also contains an additional setup with a slab-ocean and thermodynamic sea ice.
{{< /hint >}}

{{< toc >}}

## compile
First, open the terminal and go to the example directory
`cd /MITgcm/verification/aim.5l_cs`

We want to use more than 1 cpu, we use `SIZE.h_mpi`.
- go to `code` directory
- rename `SIZE.h` as `SIZE.h_single`
- rename `SIZE.h_mpi` as `SIZE.h` {{< katex >}}\rightarrow{{< /katex >}} It specifies the number of cpus as 6.
- go to `build` directory
- do `../../../tools/genmake2 -mods ../code -optfile ../../../tools/build_options/darwin_amd64_gfortran -mpi`
- if it is finished without a severe error, do `make depend`
- if it is finished without a severe error, do `make`
- if you have `mitgcmuv`, then the compliation is successful

## preparation 
The default setting integrates the model for only 10 time steps. We want to integrate the model for a couple of years. Here is the step for the model integration
- go to `run` directory
- copy all input files to here: `cp ../input/* .`
- create a sympolic link of the executable file to here: `ln -s ../build/mitgcmuv .`
- overwrite the [`data`](/files/mitgcmfiles/atmos/data) file to here

## model integration
Now, let's run the model!
- execute the run: `mpirun -np 6 ./mitgcmuv`

## analysis
We want to see the model output using `python`. I have prepared a simple JupyterLab code to start wity.
Hover the curser [here](/files/mitgcmfiles/cs_example.ipynb) and do right-click, then `Save link as...`.
In order to launch this file, open up the terminal, go to the directory where you saved this file. Then 
```
jupyter lab
```
You will have the web browser showing the `JupyterLab` interface. You can find this file in the left panel. Then double click it to open it.

## additional experiment
What if we increase the CO2 concentration in the atmosphere?

- go to `code` directory
- `../../../pkg/aim_v23/AIM_OPTIONS.h .`
- open `AIM_OPTIONS.h` and change from `#undef ALLOW_AIM_CO2` to `#define ALLOW_AIM_CO2`
- go to `build` directory
- do `make CLEAN`
- compile the code again as in [compile](/research/MITgcm/atmos/#compile)
- prepare the simulation as in [preparation](/research/MITgcm/atmos/#preparation): you may change the directory name from `run` to `run_co2` or similar.
- edit `data.aimphys` {{< katex >}}\rightarrow{{< /katex >}} add 
  ```
  aim_select_pCO2 = 1,
  aim_fixed_pCO2 = 420.E-6,
  ```
  in ` &AIM_PARAMS`
- run the model as in [model integration](/research/MITgcm/atmos/#model-integration)
