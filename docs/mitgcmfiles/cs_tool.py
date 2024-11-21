import numpy as np

def readvar_cs(odir, varname, it=None):
	"""
    Read the MITgcm output files on cubed sphere grid

    [input]
    odir    :  directory for the model output
    varname :  variable name on the file
    it      :  iteration number

    [output]
    varall  :  combined model result
    varface :  model result on each face

    [example]
    varall, varface = readvar_cs(odir, 'T', 69120)
	"""
    # metafile
    if it != None:
        metafile = odir+varname+'.{0:010d}'.format(int(it))+'.001.001.meta'
    else:
        metafile = odir+varname+'.001.001.meta'

    # read metafile
    try:
        lines = open(metafile)
    except TypeError:
        lines = iter(metafile)

    # get info from metafile
    for line in lines:
        if 'nDims' in line:
            if '3' in line:
                ndim = 3
            elif '2' in line:
                ndim = 2
        if 'dataprec' in line:
            if '64' in line:
                prec_str = '>f8'
            elif '32' in line:
                prec_str = '>f4'

    # Read variable
    if ndim==2:
        varall = np.empty([32*3, 32*4])*np.nan
        data = np.zeros([6, 32, 32])
    elif ndim==3:
        varall = np.empty([5, 32*3, 32*4])*np.nan
        data = np.zeros([6, 5, 32, 32])

    for i in range(6):
        if it !=None:
            fname = odir+varname+'.{0:010d}'.format(int(it))+'.00'+str(i+1)+'.001.data'
        else:
            fname = odir+varname+'.00'+str(i+1)+'.001.data'

        with open(fname, 'rb') as f:
            data[i] = np.fromfile(f, prec_str).reshape(-1,32,32)
    if ndim==2:
        varall[32:32*2, :32] = data[0]
        varall[32:32*2, 32:32*2] = data[1]
        varall[32*2:32*3, 32:32*2] = data[2]
        varall[32:32*2, 32*2:32*3] = data[3,:,::-1].T
        varall[32:32*2, 32*3:32*4] = data[4,:,::-1].T
        varall[:32, 32*3:32*4] = data[5,:,::-1].T
    elif ndim==3:
        varall[:, 32:32*2, :32] = data[0]
        varall[:, 32:32*2, 32:32*2] = data[1]
        varall[:, 32*2:32*3, 32:32*2] = data[2]
        varall[:, 32:32*2, 32*2:32*3] = data[3,:,:,::-1].transpose([0,2,1])
        varall[:, 32:32*2, 32*3:32*4] = data[4,:,:,::-1].transpose([0,2,1])
        varall[:, :32, 32*3:32*4] = data[5,:,:,::-1].transpose([0,2,1])

    return varall, data
