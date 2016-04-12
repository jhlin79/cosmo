import fitsio
import numpy as np
import astroML.correlation as cor
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from astropy.cosmology import FlatLambdaCDM 

cosmo = FlatLambdaCDM(H0=70, Om0=0.274, Ob0=0.0457)
fn = '~/Desktop/CIB/data/RIFSCz_short.v2.fits'
fits = fitsio.FITS(fn)

w = fits[1].where("z>0")
sel = np.arange(len(w))
np.random.shuffle(sel) 
data = fits[1][w]#[sel[:10000]]

ra = np.array(data['RA_recom'])
dec = np.array(data['DEC_recom'])
z = np.array(data['z'])
xyz = cor.ra_dec_to_xyz(ra, dec)*cosmo.comoving_distance(z)

lim = (-3000, 3000)

def plot_3d(xyz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xyz[0,:], xyz[1,:], xyz[2,:], c = 'r', marker='.', alpha=0.3)
    ax.set_xlim3d(*lim)
    ax.set_ylim3d(*lim)
    ax.set_zlim3d(*lim)

def plot_z_histogram(z):
    plt.hist(z, np.linspace(0, 0.6, 100), alpha = 0.5)
    
plot_3d(xyz)
plt.show()
plot_z_histogram(z)
plt.show()
