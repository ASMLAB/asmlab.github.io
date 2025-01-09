---
title: "Julia with MPI"
categories: ["Julia","parellel computing"]
tags: ["Julia","modelng"]
description: ""
weight: 10
---

## Parellel computing of Julia
A short note on how to configure open-mpi package for parellel computing of Julia on os x (as of 2025/01/19).

### 1. Install open-mpi
```shell
# using homebrew
brew install --build-from-source openmpi
```
It installed `open-mpi` with version 5.0.6.

### 2. Specifying the path to the mpi library
We need to set `DYLD_FALLBACK_LIBRARY_PATH` in the shell profile file. I am using zshell, so I added the following line in `.zshrc`.
```
# in .zshrc file, add
export DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/Cellar/open-mpi/5.0.6/lib"
```
Then do the following in the shell prompt to apply this change.
```
> source ~/.zshrc
```

### 3. Add MPI/MPIPreferences package in Julia
```
# tested with julia v1.11.2
julia
```
After Julia being launched, go to the package mode by pressing `]` key. Then,
```
(@v1.11) pkg> add MPI
(@v1.11) pkg> add MPIPreferences
```
Once the package is installed, come out from this package mode to julia by hitting `ctrl + C`.
Then configure the open-mpi for Julia.
```
julia> using MPIPreferences
julia> MPIPreferences.use_system_binary()
```
This will print out some information regarding open-mpi.
Since we want to use `open-mpi`, do the following.
```
julia> MPIPreferences.use_jll_binary("OpenMPI_jll")
```

### 4. Perform a test
Now, we can test whether parellel computing in Julia is working or not by executing the following simple [script](https://juliaparallel.org/MPI.jl/stable/examples/01-hello/).
```
# mpitest.jl
using MPI
MPI.Init()

comm = MPI.COMM_WORLD
print("Hello world, I am rank $(MPI.Comm_rank(comm)) of $(MPI.Comm_size(comm))\n")
MPI.Barrier(comm)
```
Then in the shell prompt,
```
> mpirun -n 4 julia mpitest.jl
Hello world, I am rank 1 of 4
Hello world, I am rank 2 of 4
Hello world, I am rank 0 of 4
Hello world, I am rank 3 of 4
```

### [Optional] Create Julia wrapper
Julia wrapper can be an alternative way for the parellel computing for Julia. It can be easily installed in Julia. 
```
$ julia
julia> using MPI
julia> MPI.install_mpiexecjl()
```
This will create `mpiexecjl` in your Julia's bin directory (maybe in ~/.julia/bin).
You may create the symbolic link of this executable file in your system.
```shell
> sudo ln -s  ~/.julia/bin/mpiexecjl /usr/local/bin/
```
Then check whether this works in the shell prompt,
```
> mpiexecjl -n 4 julia mpitest.jl
Hello world, I am rank 1 of 4
Hello world, I am rank 2 of 4
Hello world, I am rank 0 of 4
Hello world, I am rank 3 of 4
```
For more detail, please refer to the documentation of [`MPI.jl`](https://juliaparallel.org/MPI.jl/stable/usage/#Julia-wrapper-for-mpiexec)
