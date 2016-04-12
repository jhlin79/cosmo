import fitsio
import sys


def display(N):
    data = fits[1].read( rows=[N] )
    for i in xrange(len(colnames)):
        print "%20s    "%colnames[i], data[0][i]


fn = sys.argv[1]        
data_ind = int(sys.argv[2])
    
fits =  fitsio.FITS(fn)
colnames = fits[1].get_colnames()
print fits[1].get_nrows()
display(data_ind)


