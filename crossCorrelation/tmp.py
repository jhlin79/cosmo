import fitsio
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

print "reading fits map..."
galmapmask = hp.read_map('/Users/jh/Desktop/data/SDSS/mask_DR12v5_CMASS_North_512.fits')
print "map read!"

NSIDE = 512
npix = hp.nside2npix(NSIDE)
PHI_ROT = 180
rotation = [PHI_ROT, 0.0] ## (phi, theta) in deg.
r_C2G = hp.Rotator(rot=rotation, coord=['C', 'G'])
ngrid = 4*np.floor(np.sqrt(npix))  ## 16 times grid pts
theta = np.linspace(0, np.pi, ngrid)
phi = np.linspace(0, 2*np.pi, ngrid)
galmapmask_rot = np.zeros(npix)

print "iteration starts"
for t in theta:
        for p in phi:
                trot, prot = r_C2G(t, p)
                i = hp.ang2pix(NSIDE, t, p)
                j = hp.ang2pix(NSIDE, trot, prot)
                galmapmask_rot[j] = galmapmask[i]
                
hp.mollview(galmapmask_rot)
if PHI_ROT ==0:
        hp.write_map('/Users/jh/Desktop/data/SDSS/mask_DR12v5_CMASS_North_512_galactic_x4.fits', galmapmask_rot, coord='G')
else:
        hp.write_map("/Users/jh/Desktop/data/SDSS/mask_DR12v5_CMASS_North_512_galactic_x4_rot%i.fits"%(PHI_ROT), galmapmask_rot, coord='G')

                                                                
