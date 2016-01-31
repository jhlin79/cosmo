import sys
import numpy as np

fn = sys.argv[1]

fnorm = open(fn+"norm.dat")
conN = fnorm.readlines()
normD = float(conN[0].split(":")[1])
normR = float(conN[1].split(":")[1])

class pairs:
    ext     = ""
    con     = []
    sarr    = np.array([])
    muarr   = np.array([])
    mat     = np.array([])
    ns      = 0
    nmu     = 0

    def __init__(self, ext):
        
        f          = open(fn+ext+".dat")
        self.con   = f.readlines()
        self.sarr  = np.array( con[0].split() )
        self.muarr = np.array( con[1].split() )
        self.ns    = len(sarr)
        self.nmu   = len(muarr)
        self.mat   = np.array(ns-1, nmu-1)
        for l in xrange(2, ns+1):
            mat[l,:] = np.array( con[l].split() )
        f.close()


DD = pairs("DD")
RR = pairs("RR")
DR = pairs("DR")

def xi0_s(dd, rr, dr):
    nbins = dd.ns - 1
    bin_center = np.array([ mean(dd.sarr[i], dd.sarr[i+1])  for i in xrange(nbins)])
    dd_s = np.array([ sum(dd.mat[i,:]) for i in xrange(nbins)])/normD**2
    rr_s = np.array([ sum(rr.mat[i,:]) for i in xrange(nbins)])/normR**2
    dr_s = np.array([ sum(dr.mat[i,:]) for i in xrange(nbins)])/(normD*normR)
    xi_s = (dd_s - 2*dr_s + rr_s)/rr_s
