---
title: "Getting started"
categories: ["MITgcm","modeling","python"]
tags: ["MITgcm","modelng"]
description: ""
weight: 1
---

Here are a couple of things that we need to do prior to the model experiments.

{{< toc >}}

## Installing MITgcm
- [MITgcm documentation](https://mitgcm.readthedocs.io/en/latest/getting_started/getting_started.html)
- [Installing MITgcm on OSX by Jody Klymak](https://jklymak.github.io/MITgcmExampleSteadyGauss/install.html)
- [Installing MITgcm on OSX by Clark Richards](https://www.clarkrichards.org/2022/01/21/first-try-running-mitgcm/)

## Testing MITgcm
MITgcm includes a set of examples that can be run straight out of the box. For example, you can try to follow the documentation on [barotropic gyre](https://mitgcm.readthedocs.io/en/latest/examples/barotropic_gyre/barotropic_gyre.html) and see you can run the model without an issue.

## python
### miniconda
`python` can be a useful tool to analyze the results from MITgcm, and `miniconda` is one of the packages that allow you to run `python`.
You can refer to [its webpage](https://docs.anaconda.com/miniconda/miniconda-install/) for the installation of `miniconda`.

### python package
The MITgcm example that we will do has an interesting grid structure. It is called cubed sphere where the Earth is expressed as a cube. Although it is a good approach that allows us to avoid the singularity issue, it requires an attention in reading the model output. In particular, we need to combine 6 faces of the cube to make a global map. So, we will get some help from the python package called [`cubedsphere`](https://cubedsphere.readthedocs.io/en/latest/index.html)

Once you have `miniconda`, you may try to set up `cubedsphere` in the terminal app.
Here are the steps shown in its [documentation](https://cubedsphere.readthedocs.io/en/latest/installation.html)
```
conda create -n mitgcm
conda activate mitgcm
conda install -c conda-forge cubedsphere
conda install python=3.9.12
```
And let's do the followng line.
```
pip install git+https://github.com/MITgcm/xmitgcm.git
```
When you are done, you could deactivate `mitgcm` environment like this.
```
conda deactivate
```
### JupyterLab
`jupyterlab` is a useful interface in running python. To install it, you can do the following.
```
conda install -c conda-forge jupyterlab
```
Now, we are ready to analyze the model output.
In the terminal, do 
```
jupyter lab
```

This will open the web browser and launch `jupyterlab`. It consists of cells where you can do either coding, writing markdown, or just writing plain text. For more information, you can refer to its [documentation](https://jupyterlab.readthedocs.io/en/latest/).

There are other interfaces that you can do python coding. If you are familiar with one of them, you can use it!

