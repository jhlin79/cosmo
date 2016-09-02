import fitsio
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt


#####################################
##            Constants            ##
#####################################
fgal =  '/Users/jh/Desktop/data/LRG_catalog/zGT070/selected_'
fmap ={ 857:'/Users/jh/Desktop/data/Planck/HFI_SkyMap_857_2048_R2.02_full.fits'}
pcField = {353:3, 545:4, 857:5}
fmapMaskPlane = '/Users/jh/Desktop/data/Planck/HFI_Mask_GalPlane-apo2_2048_R2.00.fits'
fmapMaskPS = '/Users/jh/Desktop/data/Planck/HFI_Mask_PointSrc_2048_R2.00.fits'
NSIDE = 256
LMAX = 1024
mapFreq = 857
#####################################
##           Galaxies              ##
#####################################
theta = np.array([])
phi   = np.array([])

for i in xrange(545):
    fits = fitsio.FITS(fgal+str(i).zfill(3)+'.fits')
    theta = np.append(theta, fits[1]['dec'][:])
    phi   = np.append(phi,   fits[1]['ra'][:])
    fits.close()


theta = (-1)*theta*np.pi/180. + np.pi/2.
phi = phi*np.pi/180.



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

planckmap = hp.read_map(fmap[mapFreq])
maskPS = hp.read_map(fmapMaskPS, field=pcField[mapFreq]).astype(bool) ##field=5 for F857
maskField = 1
maskPlane = hp.read_map(fmapMaskPlane, field=maskField).astype(bool) ##field: 20% 40% 60% 70% 80%
mask = np.logical_and(maskPS, maskPlane)
planckmapMasked = hp.ma(planckmap)
planckmapMasked.mask = np.logical_not(mask)
hp.mollview(planckmapMasked, sub=(1,2,1), title="")

#######################################
##    Spherical Harmonics            ##
#######################################
plt.subplot(1, 2, 2)
cl = hp.anafast(planckmapMasked, lmax=LMAX)
ell = np.arange(len(cl))
plt.plot(ell, ell*(ell+1)*cl)
plt.xlabel('$l$')
plt.ylabel('$l(l+1) C_l$')


plt.show()


clGal = hp.anafast(galMap, lmax=LMAX, pol=False)
ellGal = np.arange(len(clGal))
plt.plot(ellGal, clGal)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('$l$')
plt.ylabel('$C_l$')
plt.ylim([10**-7, 10**-3])
plt.title('auto-power spectrum')
plt.show()


clCross = hp.anafast(galMap, planckmapMasked, lmax = LMAX)
ellCross = np.arange(len(clCross))
plt.plot(ellCross, ellCross*(ellCross+1)*clCross)
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('$l$')
plt.ylabel('$l(l+1)C_l$')
plt.title('galaxy and Planck %i GHz cross-power spectrum'%(mapFreq))
plt.show()

fw = open('cl_caro_857.out', 'w')
for i in xrange(len(clCross)):
    fw.write("%i      %.10e \n"%(ellCross[i], clCross[i]))
fw.flush()
fw.close()
