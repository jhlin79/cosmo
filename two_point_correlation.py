import fitsio
import numpy as np
import astroML.correlation as cor
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fn = '../data/specObj-dr12.fits'
fits = fitsio.FITS(fn)


w = fits[1].where("FIRSTRELEASE== 'dr12' && PLUG_RA > 135 && PLUG_RA < 225 && Z > 0.43 && Z < 0.7")
sel = np.arange(len(w))
np.random.shuffle(sel)
data = fits[1][w][sel[:10000]]

xyz = cor.ra_dec_to_xyz(data['PLUG_RA'], data['PLUG_DEC'])* data['Z']

def two_point_corr(xyz):
    bins = np.linspace(0, 1, 51)
    corr = cor.two_point(xyz.T, bins, method='landy-szalay')
    print corr
    plt.plot(corr)

def plot_3d(xyz):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xyz[0,:], xyz[1,:], xyz[2,:])

plot_3d(xyz)
plt.show()
two_point_corr(xyz)
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
