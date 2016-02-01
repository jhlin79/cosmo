import sys
import numpy as np
import matplotlib.pyplot as plt

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
    nbins   = 0
    nbinmu  = 0

    def __init__(self, ext):
        
        f          = open(fn+ext+".dat")
        self.con   = f.readlines()
        self.sarr  = np.array( self.con[0].split() )
        self.muarr = np.array( self.con[1].split() )
        self.nbins  = len(self.sarr)-1
        self.nbinmu= len(self.muarr)-1

        self.mat   = np.zeros((self.nbins, self.nbinmu))
        for l in xrange(2, self.nbins+2):
            self.mat[l-2,:] = np.array( self.con[l].split() )
        f.close()

        self.sarr = self.sarr.astype(float)
        self.muarr = self.muarr.astype(float)
        self.mat = self.mat.astype(float)


DD = pairs("DD")
RR = pairs("RR")
DR = pairs("DR")


factor = normR/normD


def xi0(dd, rr, dr):
    nbins = dd.nbins
    bin_center = [ (dd.sarr[i] + dd.sarr[i+1])/2.0  for i in xrange(nbins)]
    bin_center = np.array(bin_center)
    factor = normR/normD
    dd_s = np.array([ sum(dd.mat[i,:]) for i in xrange(nbins)])
    rr_s = np.array([ sum(rr.mat[i,:]) for i in xrange(nbins)])
    dr_s = np.array([ sum(dr.mat[i,:]) for i in xrange(nbins)])
    xi_s = (factor**2*dd_s  - factor*2*dr_s + rr_s)/rr_s
    return bin_center, xi_s/2  ##normalizer: (2l+1)/2


bins, xi = xi0(DD, RR, DR)
plt.plot(bins, xi*bins**2)
plt.xlim([0, 210])
plt.xlabel(r"$s$ (Mpc)", fontsize=16)
plt.ylabel(r"$s^2 \xi_0$ (Mpc$^2$)", fontsize=16)
plt.title(fn[:-1])
plt.show()
