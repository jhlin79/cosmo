import fitsio
import numpy as np

fn = "specObj-dr12.fits"
fits =  fitsio.FITS(fn)
nrows = fits[1].get_nrows()

def specObj_to_CMASS(drN, fr):
    w = fits[1].where("FIRSTRELEASE == 'dr%i'  && CLASS == 'GALAXY' && Z>0.43 && Z<0.7"%drN)
    data = fits[1][w]
    fr.write(data)



for drN in [7,8,12]:
    fr = fitsio.FITS("CMASS_dr%i.fits"%drN,'rw')
    specObj_to_CMASS(drN,fr)

