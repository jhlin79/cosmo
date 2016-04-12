import fitsio
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt


#####################################
##            Constants            ##
#####################################
fn = '~/Desktop/BAO/data/galaxy_DR10v8_CMASS_North.fits'
fmap =  '~/Desktop/CIB/data/HFI_SkyMap_857-field-Int_2048_R2.02_full.fits'
Nside = 32
LMAX = 1024

#####################################
##           Galaxies              ##
#####################################
fits = fitsio.FITS(fn)
wd = fits[1].where("Z > 0.43 && Z < 0.7 && WEIGHT_SYSTOT >0")
sel = np.arange(len(wd))
data = fits[1][wd]

theta = -data['DEC']*np.pi/180. + np.pi/2.
phi = data['RA']*np.pi/180.



#===  galaxies --> pixel ====

galMap = np.zeros(hp.nside2npix(NSIDE))
galPix = hp.ang2pix(NSIDE, theta, phi)

for pix in galPix:
    galMap[pix] += 1

countMean = np.average(galMap)
galMap = galMap - countMean


######################################
##           Planck Map             ##
######################################
planck857 = hp.read_map(fmap)
## plot planck map
hp.mollview(planck857)



#######################################
##    Spherical Harmonics            ##
#######################################
cl = hp.anafast(planck857, lmax=LMAX)
ell = np.arange(len(cl))
plt.plot(ell, ell * (ell+1) * cl)
plt.show()
