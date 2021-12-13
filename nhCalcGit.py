import numpy as np
import math
from scipy.integrate import quad

def nhcalc():


#some cosmology    

    h = .7
    omegam = 0.3
    omegalambda=0.7
    w=-1

#cluster + model parameters

    arcminToKpc = np.power(1.913*60.,3) #kpc/arcsec

    kpcToCm = np.power(3.086e21,3)

    z = [0.1042]

#must input XSPEC normalization somewhere in here to calculate n_e (electron density), and temperature to calculate entropy
#all of my XSPEC fits are normalized to arcmin^-2, so this is an additional term in the calculations

#other additional values needed for different geometrical region configurations...see some examples below

    V = Varcmin*arcminToKpc*kpcToCm #cm^3

    i = 89. #degrees

#subtracting from 90 because angle is given to be between line of sight and long axis->need to convert to planar

    irad = i*(np.pi/180.) #converting degrees to radians because python trig takes radians

#hubble distance

    Dh = 3000*(h**(-1)) #Mpc
    Dhcm = Dh*3.086e24

#integral to factor out hubble flow in order to get comoving distance

    def integrand(zvar):
        return 1./(np.sqrt(omegam*np.power((1+zvar),3.)+omegalambda*np.power((1+zvar),(3*(1+w)))))

    Dc = Dh*quad(integrand,0,z[0])[0]

#can use the comoving distance to get the angular diameter distance

    Da = Dc/(1.+z[0]) #Mpc

    Dacm = Da*3.086e24

    ne = np.power(np.cos(irad)*norm*areascal*4.*np.pi*((1.+z[0])**2)*(1./1.2e-14)*(Dacm**2)*(V**-1),1./2.)

#for spherical geometry...

#    ne = (3.6*norm*areascal*np.cos(irad)*((1.+z[0])**2)*(1.08*10.**-10)*(Da**2)*(r**-3))**(1./2.) #cm^-3

#for cylindrical geometry...

#    ne = (1.2*norm*areascal*np.cos(irad)*((1.+z[0])**2)*(1.08*10.**-10)*(Da**2)*(r**-2)*(lobs**-1))**(1./2.) #cm^-3

#for a trapezoid geometry...

#    ne = (1.2*norm*areascal*np.cos(irad)*((1.+z[0])**2)*(1.08*10.**-10)*(Da**2)*(H**-1)*(lobs**-1)*((a+b)/2.)**-1)**(1./2.)

#for a prolate ellipsoid geometry...

#    ne = (1.2*norm*areascal*np.cos(irad)*((1.+z[0])**2)*(1.08*10.**-10)*(Da**2)*(b**-2)*(a**-1))**(1./2.)

#Volume calculated with deprojGit.py script

    siglow = np.sqrt(np.power(norm-normlow,2)*np.power(np.cos(irad)*4.*np.pi*0.5*areascal*(Dacm**2)*((1.+z[0])**2)*(1.2/1.e-14)*(V**-1)*np.power(np.cos(irad)*1.2*norm*areascal*(Dacm**2)*((1.+z[0])**2)*(1.2/1.e-14)*(V**-1),-1./2.),2))
    sighigh = np.sqrt(np.power(norm-normhigh,2)*np.power(np.cos(irad)*4.*np.pi*0.5*areascal*(Dacm**2)*((1.+z[0])**2)*(1.2/1.e-14)*(V**-1)*np.power(np.cos(irad)*1.2*norm*areascal*(Dacm**2)*((1.+z[0])**2)*(1.2/1.e-14)*(V**-1),-1./2.),2))

#cylindrical geometry

#    sighigh = 0.5*(normhigh)*(1.2*norm*areascal*np.cos(irad)*((1.+z[0])**2)*(1./1.e-14)*(Dacm**2)*(r**-2)*(lobs**-1))**(-1./2.)

#for ellipsoid geometry

#    siglow = 0.5*(norm-normlow)*(1.2*norm*areascal*np.cos(irad)*((1.+z[0])**2)*(1.08*10.**-10)*(Da**2)*(b**-2)*(a**-1))**(-1./2.) #cm^-3

#    sighigh = 0.5*(normhigh-norm)*(1.2*norm*areascal*np.cos(irad)*((1.+z[0])**2)*(1.08*10.**-10)*(Da**2)*(b**-2)*(a**-1))**(-1./2.)

    vol = np.pi*r**2*((lobs)/np.cos(irad)) #Mpc
#    print (vol)

    volcm = vol*(3.086*10.**24)**3 #cm
    me = 9.1*10**-31 #kg
    mh = 1.67*10**-27 #kg
    rho = (me+mh)*(ne+1.2*ne) #kg/cm^3

    mtot = rho*volcm #kg
    mtotsolar = mtot*(1./(1.99*10**30))

    s = t*np.power(ne,-2./3.)

    ssiglow = np.sqrt(np.power((-2./3.)*t*np.power(ne,-5./3.),2)*np.power(siglow,2) + np.power(np.power(ne,-2./3.),2)*np.power(tlow,2))

    ssighigh = np.sqrt(np.power((-2./3.)*t*np.power(ne,-5./3.),2)*np.power(sighigh,2) + np.power(np.power(ne,-2./3.),2)*np.power(thigh,2))


nhcalc()
