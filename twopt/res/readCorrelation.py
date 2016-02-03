import sys
import numpy as np
import matplotlib.pyplot as plt


#################################################################
##        Container of -DD.dat -DR.dat -RR.dat results         ##
#################################################################
class pairs:

    def __init__(self, ext):
        f = open(fn + ext + ".dat")
        self.ext = ext
        self.con = f.readlines()
        self.sarr = np.array(self.con[0].split())
        self.muarr = np.array(self.con[1].split())
        self.nbins = len(self.sarr) - 1
        self.nbinmu = len(self.muarr) - 1

        self.mat = np.zeros((self.nbins, self.nbinmu))
        for l in xrange(2, self.nbins + 2):
            self.mat[l - 2, :] = np.array(self.con[l].split())
        f.close()

        self.sarr = self.sarr.astype(float)
        self.muarr = self.muarr.astype(float)
        self.mat = self.mat.astype(float)


###################################################################
##         This class sumarizes all the pair counts.             ##
##         It can output correlation functions and figures.      ##
###################################################################
class twoRes:

    def __init__(self, fn):
        fnorm = open(fn + "-norm.dat")
        conN = fnorm.readlines()
        normD = float(conN[0].split(":")[1])
        normR = float(conN[1].split(":")[1])

        self.DD = pairs("-DD")
        self.RR = pairs("-RR")
        self.DR = pairs("-DR")
        self.factor = normR / normD

    def sbinCenters(self):
        nbins = self.DD.nbins
        return np.array([(self.DD.sarr[i] + self.DD.sarr[i + 1]) / 2.0 for i in xrange(nbins)])

    # This function averages out the mu dependence.
    def xi0(self):
        nbins = self.DD.nbins
        dd_s = np.array([sum(self.DD.mat[i, :]) for i in xrange(nbins)])
        rr_s = np.array([sum(self.RR.mat[i, :]) for i in xrange(nbins)])
        dr_s = np.array([sum(self.DR.mat[i, :]) for i in xrange(nbins)])
        xi_s = (self.factor**2 * dd_s - self.factor * 2 * dr_s + rr_s) / rr_s
        return xi_s / 2  # normalizer: (2l+1)/2

    def plot_xi0(self):
        plt.plot(self.sbinCenters(), self.xi0() * self.sbinCenters()**2)
        plt.xlim([0, 210])
        plt.xlabel(r"$s$ (Mpc)", fontsize=16)
        plt.ylabel(r"$s^2 \xi_0$ (Mpc$^2$)", fontsize=16)
        plt.title(fn)
        plt.show()

    # Transform xi0 to power spectrum
    def ps(self, kmax=1.0, n=50):
        sarr = self.sbinCenters()
        ds = sarr[1] - sarr[0]
        xi0 = self.xi0()
        karr = np.linspace(kmax / n, kmax, n)
        pwarr = np.linspace(0, 0, n)
        for i in xrange(n):
            k = karr[i]
            pwarr[i] = sum(xi0 * sarr * np.sin(k * sarr) * ds / k)
        return pwarr

    def plot_ps(self, type, kmax=0.3, n=100):
        karr = np.linspace(kmax / n, kmax, n)
        pwarr = self.ps(kmax, n)
        # plot k times P(k)
        if type == 'kp':
            plt.plot(karr, karr * pwarr * np.pi**2 / (2 * np.pi**2))
            plt.xlabel(r"$k$ (Mpc$^{-1}$)", fontsize=16)
            plt.ylabel(r"$kP(k)/2\pi^2$ (Mpc$^2$)", fontsize=16)
            plt.title("power spectrum")
            plt.show()
        # Log plot of the power spectrum.
        elif type == 'log':
            plt.plot(np.log10(karr), np.log10(pwarr * np.pi**2))
            plt.xlabel(r"$\log_{10} k$", fontsize=16)
            plt.ylabel(r"$\log_{10} P(k)$", fontsize=16)
            plt.title("power spectrum")
            plt.xlim([-2.0, -0.5])
            plt.ylim([3.2, 5.1])
            plt.show()


################################
##           main             ##
################################
if __name__ == "__main__":
    fn = sys.argv[1]
    res = twoRes(fn)
    res.plot_xi0()
    res.plot_ps('kp')
    res.plot_ps('log')
