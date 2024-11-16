---
title: "coupled"
categories: ["modeling","MITgcm"]
tags: ["modeling"]
description: ""
weight: 4
---

MITgcm can be an atmosphere-ocean coupled model using its own coupler. 
There is a verification called `cpl_aim+ocn`, and it is a coupled version of atmospheric and oceanic model on cubed sphere grid that we did so far.
The instruction below can be found in `README` file in `cpl_aim+ocn` to run the coupled simulation.

{{< hint type=note icon=gdoc_check title=README.md >}}
### Atmosphere-Ocean coupled set-up example "cpl_aim+ocn"
using simplified atmospheric physics (AIM), in realistic configuration (orography
& continent) with land and seaice component, on cubed-sphere (cs-32) grid.
{{< /hint >}}

{{< toc >}}

## overview
Uses "in-house" MITgcm coupler
(pkg/atm_ocn_coupler, pkg/compon_communic, pkg/atm_compon_interf, pkg/ocn_compon_interf )
with each component config and customized src code in: code_cpl, code_atm, code_ocn ;
and input parameter files in: input_cpl, input_atm, input_ocn.

- Atmos set-up and parameter is similar to "aim_5l_cs/" experiment
- Ocean set-up and parameter is similar to "global_ocean.cs32x15/" experiment

Requires the use of MPI; as default, use 1 proc for each component.


## cleaning
If you compile the code for the first time, you do not need to do this. But if you want to redo compilation, then it is good to clean up the existing files.

To clean everything:
```
  ../../tools/run_cpl_test 0
```

## compile
We need to do one thing to avoid a compiling error that might come from the compiler version issue.
Hover the curser [here](/mitgcmfiles/setdir.c) and do right-click, then click `Save link as...`.
Save this file in `code_cpl` as `setdir.c`.

Now, we will compile three models: coupler, ocean model and atmospheric model with the following line.
```
  ../../tools/run_cpl_test 1 -of ../../tools/build_options/darwin_amd64_gfortran
```

## integration with default configuration
To run primary setup, thermodynamic seaice only (no seaice dynamics):
```
  ../../tools/run_cpl_test 2
  ../../tools/run_cpl_test 3
```

## integration with modification
Step 2 above copies input files and directories, step 3 runs the coupled model.

To run secondary test (with seaice dynamics as part of ocean component), using input parameter files in: input_cpl.icedyn, input_atm.     icedyn, input_ocn.icedyn:
```
  ../../tools/run_cpl_test 2 icedyn
  ../../tools/run_cpl_test 3
```
## use more cpus
The default setting uses total 3 cpus (1 for each), which may not give you the best speed of integration.
We can use more than 1 cpus for each component to speed up. 
Let's first check the number of cpus we can use. In terminal,
```
sysctl -n hw.ncpu
```
For me, I have 8 cpus. So, I am going to use 4 cpus for the atmospheric component, 2 cpus for the oceanic component and 1 for the coupler.


## model results
Results are written in rank_{0,1,2} dir, for coupler, ocean and atmos comp. respectively


## analysis
Note:<br>
To check the results, monitor output could be compared to reference (in results/) using "run_cpl_test", step 4.<br>
For primary set-up:
```
  ../../tools/run_cpl_test 4
```
and for secondary test:
```
  ../../tools/run_cpl_test 4 icedyn
```
but this requires, in your path, a simple comparison script "comp_res"
(which is not provided here but could be found in:
 http://wwwcvs.mitgcm.org/viewvc/MITgcm/MITgcm_contrib/jmc_script/ ), along with some other files found in this archive.
