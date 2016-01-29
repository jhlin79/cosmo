from astropy.cosmology import FlatLambdaCDM
import numpy as np


Om = 0.274
Obh2 = 0.0224
H0 = 70
h = 0.7
b1 = 0.313*(Om * h**2)**(-0.419) * ( 1 + 0.607*(Om * h**2)**0.674  )
b2 = 0.238*(Om * h**2)**0.223
zd = 1291 * (Om * h**2)**0.251 * (1 + b1*(Obh2)**b2) / (1 + 0.659*(Om * h**2)**0.828)
Theta = 2.73/2.7
R = lambda z:31.5*Obh2 * Theta**(-4) *1000 / z
Rd = R(zd)
zeq = 25000*(Om * h**2)*Theta**(-4)
keq = 0.0746*(Om * h**2)*Theta**(-2)
Req = R(zeq)
rs = 2.0/(3*keq) * np.sqrt(6.0/Req) * np.log( ( np.sqrt(1+Rd) + np.sqrt(Rd + Req)  ) / ( 1 + np.sqrt(Req) ) )


cosmo = FlatLambdaCDM(H0=70, Om0=0.274, Ob0=0.0457 )


def Hz(z):
    return H0 * np.sqrt( Om*(1+z)**3 + (1-Om))

def Dv(z):
    Da = cosmo.angular_diameter_distance(z).value
    return (3.0*10**5 * z * (1+z)**2 * Da**2 / Hz(z))**(1.0/3.0)


print 'rs          :', rs
print 'Dv(0.57)    :', Dv(0.57)
print 'Dv(0.57)/rs :', Dv(0.57)/rs
