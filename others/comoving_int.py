import scipy.integrate as itg
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

class dc:
    Om = 0.274
    z_min = 0.4
    z_max = 0.7
    z_num = 51
    para = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    DH = 3000/0.7
    zarr = np.array([])
    dcInt = np.array([])
    dcFit = np.array([])
    
    def __init__(self, p1, p2, p3, p4, p5):
        self.para[0] = p1
        self.para[1] = p2
        self.para[2] = p3
        self.para[3] = p4
        self.para[4] = p5
        self.zarr = np.linspace(self.z_min, self.z_max, self.z_num)
        self.dcInt = np.linspace(0.0, 0.0, self.z_num)
        self.dcFit = np.linspace(0.0, 0.0, self.z_num)
        self.dcIntGen()
        self.dcFitGen()

    def integrand(self, z):
        return self.DH/ np.sqrt((1.0 + self.Om*(3*z + 3*z**2 + z**3)))

    def dcIntFun(self, z):
        return itg.quad(self.integrand, 0, z)[0]

    def dcFitFun(self, z):
        return self.DH*self.para[2]*z / np.sqrt( 1. + self.para[0]*z**self.para[3] + self.para[1]*z**self.para[4])

    def dcIntGen(self):
        for i in xrange(self.z_num):
            self.dcInt[i] = itg.quad(self.integrand, 0, self.zarr[i])[0]

    def dcFitGen(self):
        for i in xrange(self.z_num):
            self.dcFit[i] = self.dcFitFun(self.zarr[i])

    def err(self):
        sm = 0.0
        for i in xrange(self.z_num):
            sm += (self.dcInt[i] - self.dcFit[i])**2

        return np.sqrt(sm)
    
    def Plot(self):
        p1 ,= plt.plot(self.zarr, self.dcInt)
        p2 ,= plt.plot(self.zarr, self.dcFit)
        plt.legend([p1,p2], ["quad", "Fit"])
        plt.show()


    def fit_para(self, i):
        res = minimize(self.set_para, self.para[i], args=(i,), method='Nelder-Mead', tol=1e-6 )
        self.para[i] = res.x

    def set_para(self, p, i):
        self.para[i] = p
        self.dcFitGen()
        return self.err()

    def goFit(self):
        for i in [2, 0, 1, 3, 4]:
            dcObj.fit_para(i)

    def fit_para_all(self):
        res = minimize(self.set_para_all, self.para, method='Nelder-Mead', tol=1e-6 )


    def set_para_all(self, para):
        self.para = para
        self.dcFitGen()
        return self.err()


    def relErr(self,z):
        return (dcObj.dcFitFun(z)-dcObj.dcIntFun(z))/dcObj.dcIntFun(z)
        
#dcObj = dc(0.477739354, 0.08925765, 0.97798768, 1.37515307, 1.94760834)
dcObj =  dc(0.55109459, 0.04424543, 0.99033654, 1.26811119, 2.27075546)
#for i in xrange(20):
#    dcObj.goFit()
dcObj.fit_para_all()

print "fitting parameters: ", dcObj.para

for z in [0.4, 0.5, 0.6, 0.7]:
    print "z=%.4f  quad=%.6f  fit=%.6f  percErr=%.4e"%( z, dcObj.dcIntFun(z), dcObj.dcFitFun(z), dcObj.relErr(z))

dcObj.Plot()
