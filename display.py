import fitsio
import sys

def display(N):
    data = fits[1].read( rows=[N] )
    for i in xrange(len(colnames)):
        print "%20s    "%colnames[i], data[0][i]

data_ind = int(sys.argv[1])
fn = "~/Desktop/BAO/data/galaxy_DR10v8_CMASS_North.fits"
fits =  fitsio.FITS(fn)
colnames = fits[1].get_colnames()
print fits[1].get_nrows()
display(data_ind)


