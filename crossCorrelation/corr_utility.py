import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

def cl_read(fn):
    f = open(fn)
    con = f.readlines()
    ell = []
    cl  = []
    for line in con:
        line = line.split()
        ell.append( int(line[0]) )
        cl.append( float(line[1]))
    return ell, cl

def cl_binned(l, cl, binSize): 
    nbins = len(l)/binSize
    l_bin = []
    cl_bin = []
    for ib in xrange(nbins):
        l_bin.append(ib*binSize + binSize/2 + l[0])
        cl_bin.append( np.average( cl[ib*binSize:(ib+1)*binSize])   )

    return l_bin, cl_bin

def cl_save(l, cl, fn):
    fw = open(fn, 'w')
    for i in xrange(len(cl)):
        fw.write("%i      %.10e \n"%(l[i], cl[i]))
    fw.flush()
    fw.close()
    return

def cl_plot(cl, binSize=1, lmin=0, style='bo', alpha=0.7):
    ell = np.arange(len(cl))
    ell_bin, cl_bin = cl_binned(ell[lmin:], cl[lmin:], binSize)
    plt.plot(ell_bin, cl_bin, style, alpha=alpha)
    return
    
def radec2thetaphi(ra, dec):
    theta = (-1)*dec*np.pi/180. + np.pi/2.
    phi = ra*np.pi/180. 
    return theta, phi

    
    
        
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
