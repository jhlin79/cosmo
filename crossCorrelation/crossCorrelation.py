import fitsio
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt


#####################################
##            Constants            ##
#####################################
fgal =  '/Users/jh/Desktop/data/SDSS/data/galaxy_DR12v5_CMASS_North.fits'
fgalMask = '/Users/jh/Desktop/data/SDSS/data/mask_DR12v5_CMASS_North.fits'
fmap ='/Users/jh/Desktop/data/Planck/HFI_SkyMap_857_2048_R2.02_full.fits'
fmapMaskPlane = '/Users/jh/Desktop/data/Planck/HFI_Mask_GalPlane-apo2_2048_R2.00.fits'
fmapMaskPS = '/Users/jh/Desktop/data/Planck/HFI_Mask_PointSrc_2048_R2.00.fits'
NSIDE = 256
LMAX = 1024

#####################################
##           Galaxies              ##
#####################################

fits = fitsio.FITS(fgal)
#wd = fits[1].where("Z > 0.43 && Z < 0.7 && WEIGHT_SYSTOT >0")
wd = fits[1].where("Z>0")
sel = np.arange(len(wd))
data = fits[1][wd]

theta = -data['DEC']*np.pi/180. + np.pi/2.
phi = data['RA']*np.pi/180.

r_C2G = hp.Rotator(coord=['C', 'G'])
theta, phi = r_C2G(theta, phi)


#===  galaxies --> pixel ====

galMap = np.zeros(hp.nside2npix(NSIDE))
galPix = hp.ang2pix(NSIDE, theta, phi)

for pix in galPix:
    galMap[pix] += 1

galMap_Ngal = len(theta)
galMap_Npix = 0  ## keep track of the number of pixels covered
for i in xrange(len(galMap)):
    if galMap[i] == 0:
        galMap[i] = hp.UNSEEN
    else:
        galMap_Npix+=1

countMean = float(galMap_Ngal)/galMap_Npix

for i in xrange(len(galMap)):
    if galMap[i] != hp.UNSEEN:
        galMap[i] = (galMap[i] - countMean)/countMean
print countMean

hp.mollview(galMap)#, rot=(180,0,0))
plt.show()

######################################
##           Planck Map             ##
######################################

planck857 = hp.read_map(fmap)
maskPS = hp.read_map(fmapMaskPS, field=5).astype(bool) ##field=5 for F857
maskPlane = hp.read_map(fmapMaskPlane, field=1).astype(bool) ##field=0 for 20% coverage
mask = np.logical_and(maskPS, maskPlane)
planck857Masked = hp.ma(planck857)
planck857Masked.mask = np.logical_not(mask)

hp.mollview(planck857Masked)
plt.show()



#######################################
##    Spherical Harmonics            ##
#######################################

cl = hp.anafast(planck857Masked, lmax=LMAX)
ell = np.arange(len(cl))
plt.plot(ell, ell * (ell+1) * cl)
plt.xlabel('$l$')
plt.ylabel('$l(l+1) C_l$')
plt.title('Planck 857 GHz auto-power spectrum')
plt.show()


clGal = hp.anafast(galMap, lmax=LMAX)
ellGal = np.arange(len(clGal))
plt.plot(ellGal, clGal)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('$l$')
plt.ylabel('$C_l$')
plt.title('CMASS North dr12 auto-power spectrum')
plt.xlim([0, LMAX])
plt.ylim([10**-6, 10**1])
plt.show()

clCross = hp.anafast(galMap, planck857Masked, lmax = LMAX)
ellCross = np.arange(len(clCross))
plt.plot(ellCross, ellCross*(ellCross+1)*clCross)
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('$l$')
plt.ylabel('$l(l+1)C_l$')
plt.title('galaxy and Planck 857 GHz cross-power spectrum')
plt.show()

fw = open('cl_cmass_857.out', 'w')
for i in xrange(len(clCross)):
    fw.write("%i      %.10e \n"%(ellCross[i], clCross[i]))
fw.flush()
fw.close()
