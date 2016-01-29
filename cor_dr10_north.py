import fitsio
import numpy as np
import astroML.correlation as cor
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from astropy.cosmology import FlatLambdaCDM

def two_point_corr(xyz, xyz_rand):
    bins = np.linspace(bin_min, bin_max, nbins)
    corr = cor.two_point(xyz.T, bins, method='landy-szalay', data_R = xyz_rand.T)
    print corr
    s_ls = bins[:-1]+(bin_max-bin_min)/(2*nbins)
    plt.plot(s_ls, s_ls**2 * corr)


def plot_3d(xyz, xyz_rand):
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')
    ax1.scatter(xyz[0,:], xyz[1,:], xyz[2,:])
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z')
    ax1.view_init(elev=90)
    ax2.scatter(xyz_rand[0,:], xyz_rand[1,:], xyz_rand[2,:])
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('z')
    ax2.view_init(elev=90)

def proper_distance(z):
    return cosmo.comoving_distance(z) / (1+z)


cosmo = FlatLambdaCDM(H0=70, Om0=0.274, Ob0=0.0457)
fn = '~/Desktop/BAO/data/galaxy_DR10v8_CMASS_North.fits'
fn_rand = '~/Desktop/BAO/data/random1_DR10v8_CMASS_North.fits' 
bin_min = 29
bin_max = 200.0
nbins = 22
ndata = 5000
ndataR = 50000

fits = fitsio.FITS(fn)
fits_rand = fitsio.FITS(fn_rand)

w = fits[1].where("Z > 0.43 && Z < 0.7")
sel = np.arange(len(w))
np.random.shuffle(sel)
data = fits[1][w][sel[:min(ndata, len(w))]]

w = fits_rand[1].where("Z > 0.43 && Z < 0.7")
sel = np.arange(len(w))
np.random.shuffle(sel)
data_R = fits_rand[1][w][sel[:min(ndataR, len(w))]]

xyz = cor.ra_dec_to_xyz(data['RA'], data['DEC'])* proper_distance(data['Z'])

xyz_rand = cor.ra_dec_to_xyz(data_R['RA'], data_R['DEC'])* proper_distance(data_R['Z'])


#plot_3d(xyz, xyz_rand)
#plt.show()
two_point_corr(xyz, xyz_rand)

plt.xlabel('z')
plt.ylabel(r"$xi$")
plt.show()



##============================================================##
##                        Results                             ##
##============================================================##

## size:100000
##[ 0.70176471  0.49961308  0.43241497  0.37154842  0.31017746  0.24798244
##  0.19168444  0.13932903  0.09201617  0.0492623   0.01196304 -0.02015125
## -0.04640968 -0.06557794 -0.07843541 -0.08423552 -0.08600951 -0.08351398
## -0.07758738 -0.06881051 -0.05946446 -0.04756083 -0.03524165 -0.02098275
## -0.00545036  0.0114628   0.02809498  0.04682281  0.06529613  0.086147
##  0.10158668  0.11337286  0.11831161  0.12003855  0.11791493  0.10618294
##  0.08862253  0.05896533  0.02111982 -0.02917854 -0.08813564 -0.16263832
## -0.25591232 -0.34724491 -0.43452608 -0.52322997 -0.61538424 -0.69220245
## -0.72754675 -0.7332965 ]
