import fitsio
import numpy as np
import matplotlib.pyplot as plt
import sys

freq = sys.argv[1]
cmapName = 'jet'
size = 8
bg = 'LightCyan'
valueMin = 0
valueMax = 6000
#### Read Fits file ####
fn = '~/Desktop/CIB/data/COM_PCCS_'+freq+'_R2.01.fits'
fits = fitsio.FITS(fn)
w = fits[1].where("APERFLUX > 0")
sel = np.arange(len(w))
np.random.shuffle(sel) 
data = fits[1][w]

ra = np.array(data['RA'])
dec = np.array(data['DEC'])
flux = np.array(data['APERFLUX'])

#### convert coordinate to degree ####
ra  -= 180
ra  *= np.pi / 180.0
dec *= np.pi / 180.0


def plot_mollweide(ra, dec, flux):
    fluxMin = flux.min()
    fluxMax = flux.max()
    print fluxMin, fluxMax
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='mollweide', axisbg =bg)
    ax.grid()
    ax.scatter(ra, dec, c=flux, s=size, lw=0, vmin=valueMin, vmax=valueMax, cmap=cmapName, alpha = 0.75)
    plt.title("Planck Flux @ %s GHz"%(freq))
    
def plot_flux_histogram(flux):
    plt.hist(flux, np.linspace(flux.min(), flux.max()/10, 100), alpha = 0.5)
    plt.title("Planck Flux Histogram at %s GHz"%(freq))
    plt.xlabel("aperture flux (mJy)")
    
plot_mollweide(ra, dec, flux)
plt.show()
plot_flux_histogram(flux)
plt.show()
