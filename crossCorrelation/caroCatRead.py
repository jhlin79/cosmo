import fitsio
import numpy as np
import sys
import matplotlib.pyplot as plt 



selNum = sys.argv[1] ## 0 < selNum < 544

fn = "/Users/jh/Desktop/data/LRG_catalog/selected_%s.fits"%(selNum.zfill(3))
fits = fitsio.FITS(fn)
data = fits[1][:]
cmodelmag = np.array(data['cmodelmag'])
w1 = np.array(data['w1_mag'])
r_band = cmodelmag[:,2]
i_band = cmodelmag[:,3]

#x = np.linspace(-4, 5, 100)
#y = 0.249*x + 2.0
#plt.plot(x,y, alpha=0.5)

plt.scatter(r_band-i_band, r_band-w1, c='r', alpha=0.5, s=5)
plt.xlim([-3,5])
plt.xlabel('r - i')
plt.ylabel('r - 3.4$\mu m$')
plt.show()
