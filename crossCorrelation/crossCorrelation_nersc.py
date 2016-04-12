import fitsio
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt


#####################################
##            Constants            ##
#####################################
fgal =  '/global/homes/c/chienhao/data/CMASS/galaxy_DR12v5_CMASS_North.fits'
fmap ={ 857:'/global/homes/c/chienhao//data/Planck/HFI_SkyMap_857_2048_R2.02_full.fits', 545:'/global/homes/c/chienhao//data/Planck/HFI_SkyMap_545_2048_R2.02_full.fits', 353:'/global/homes/c/chienhao//data/Planck/HFI_SkyMap_353_2048_R2.02_full.fits'}
pcField = {353:3, 545:4, 857:5}
fmapMaskPlane = '/global/homes/c/chienhao/data/Planck/HFI_Mask_GalPlane-apo0_2048_R2.00.fits'
fmapMaskPS = '/global/homes/c/chienhao/data/Planck/HFI_Mask_PointSrc_2048_R2.00.fits'
NSIDE = 512
LMAX = 512
mapFreq = 353
#####################################                                                                                                                                            
##           Galaxies              ##                                                                                                                                            
#####################################                                                                                                                                            
 
fits = fitsio.FITS(fgal)
wd = fits[1].where("Z>0")
sel = np.arange(len(wd))
data = fits[1][wd]

theta = -data['DEC']*np.pi/180. + np.pi/2.
phi = data['RA']*np.pi/180.

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

countMean = galMap_Ngal/galMap_Npix

for i in xrange(len(galMap)):
    if galMap[i] != hp.UNSEEN:
        galMap[i] = (galMap[i] - countMean)/countMean


#hp.mollview(galMap, rot=(180,0,0))
#plt.show()

######################################                                                                                                                                           
##           Planck Map             ##                                                                                                                                           
######################################                                                                                                                                           

planck857 = hp.read_map(fmap[mapFreq])
maskPS = hp.read_map(fmapMaskPS, field=pcField[mapFreq]).astype(bool) ##field=5 for F857
maskFields = [0,1,2]
#maskFields = [3,4,5]
for i in xrange(len(maskFields)):
    f = maskFields[i]
    maskPlane = hp.read_map(fmapMaskPlane, field=f).astype(bool) ##field: 20% 40% 60% 70% 80%
    mask = np.logical_and(maskPS, maskPlane)
    planck857Masked = hp.ma(planck857)
    planck857Masked.mask = np.logical_not(mask)
    hp.mollview(planck857Masked, sub=(len(maskFields),2,2*i+1), title="")

#######################################                                                                                                                                          
##    Spherical Harmonics            ##
#######################################                                                                                                                                          
    plt.subplot(len(maskFields), 2, 2*i+2)
    cl = hp.anafast(planck857Masked, lmax=LMAX)
    ell = np.arange(len(cl))
    plt.plot(ell, ell*(ell+1)*cl)
    plt.xlabel('$l$')
    plt.ylabel('$l(l+1) C_l$')


plt.show()


clGal = hp.anafast(galMap, lmax=LMAX)
ellGal = np.arange(len(clGal))
plt.plot(ellGal, clGal)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('$l$')
plt.ylabel('$C_l$')
plt.title('CMASS North dr12 auto-power spectrum')
plt.show()


#clCross = hp.anafast(planck857Masked, galMap, lmax = LMAX)
#ellCross = np.arange(len(clCross))
#plt.plot(ellCross, clCross)
##plt.xscale('log')
##plt.yscale('log')
#plt.xlabel('$l$')
#plt.ylabel('$C_l$')
#plt.title('CMASS North dr12 and Planck 857 GHz cross-power spectrum')
#plt.show()
