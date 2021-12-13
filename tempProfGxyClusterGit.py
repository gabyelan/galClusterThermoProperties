import math
import numpy as np
import matplotlib.pyplot as plt


def tempprofGxyCluster():

#this code is to plot the self-similar temperature profile from Vikhlinin+05
#universal temperature profile from Pratt+2007
#universal temperature profile from Ghirardini+2019
#input numbers are for A98N

    h = 0.7 #1/Hubble const.
    tav = 2.9 #average temperature in keV
    r180 = 1.95*(h**(-1.))*np.power((tav/10.),1./2.) #the radius at which the density is 180 times the critical density of the universe in Mpc
    r200 = 1.2 #Mpc
    r500 = r200/1.6
    t500 = 2.9

    r = np.linspace(0.125*r200,1.2*r200,50)

#    t = tav*(1.22-1.2*(r/r180))

    t = tav*(1.19-(0.74*r/r200))

    sector01t = 2.91 #keV
    sector01tdeproj = 2.94
    sector01r = 0.275 #Mpc

    sector02t = 2.70
    sector02tdeproj = 3.2
    sector02r = 0.71

    sector03t = 1.29
    sector03r = 1.19

    sector01wT = 2.93
    sector01wTdeproj = 2.9
    sector01wR = 0.275

    sector02wT = 2.53
    sector02wTdeproj = 3.0
    sector02wR = 0.71

    sector03wT = 1.2
    sector03wR = 1.19

    plt.plot(r/r180,t,label='V+05 SS')
    plt.errorbar(sector01r/r180,sector01t,xerr=[[0.175/r180],[0.175/r180]],yerr=[[0.34],[0.35]],fmt='g',markersize=14,label='a98n')
    plt.errorbar(sector02r/r180,sector02t,xerr=[[0.26/r180],[0.26/r180]],yerr=[[0.97],[1.68]],fmt='g',markersize=14,)
    plt.errorbar(sector03r/r180,sector03t,xerr=[[0.22/r180],[0.22/r180]],yerr=[[0.33],[0.62]],fmt='g',markersize=14,)
    plt.errorbar(sector01wR/r180,sector01wT,xerr=[[0.175/r180],[0.175/r180]],yerr=[[0.3],[0.32]],fmt='deeppink',markersize=14,label='a98w')
    plt.errorbar(sector02wR/r180,sector02wT,xerr=[[0.26/r180],[0.26/r180]],yerr=[[0.5],[0.8]],fmt='deeppink',markersize=14)
    plt.errorbar(sector03wR/r180,sector03wT,xerr=[[0.22/r180],[0.22/r180]],yerr=[[0.2],[0.3]],fmt='deeppink',markersize=14)
    plt.title('A98N+W Sector Profile Compared to V05 SS')
    plt.ylabel('T[keV]')
    plt.xlabel('r/r180')
    plt.legend()
    plt.savefig('a98nSector.5.a98wSector.2.tempProf.compSS.png')
    plt.show()


    plt.plot(r/r200,t,label='Pratt+07')
    plt.errorbar(sector01wR/r200,sector01wTdeproj,xerr=[[0.175/r180],[0.175/r180]],yerr=[[0.34],[0.35]],fmt='deeppink',marker='.')
    plt.errorbar(sector02wR/r200,sector02wTdeproj,xerr=[[0.26/r180],[0.26/r180]],yerr=[[1.07],[1.86]],fmt='deeppink',marker='.',label='a98w deproj')
    plt.errorbar(sector03wR/r200,sector03wT,xerr=[[0.22/r180],[0.22/r180]],yerr=[[0.33],[0.62]],fmt='deeppink',marker='.')
    plt.errorbar(sector01r/r200,sector01tdeproj,xerr=[[0.175/r180],[0.175/r180]],yerr=[[0.34],[0.35]],fmt='g.')
    plt.errorbar(sector02r/r200,sector02tdeproj,xerr=[[0.26/r180],[0.26/r180]],yerr=[[1.07],[1.86]],fmt='g.',label='a98n deproj')
    plt.errorbar(sector03r/r200,sector03t,xerr=[[0.22/r180],[0.22/r180]],yerr=[[0.33],[0.62]],fmt='g.')
 #   plt.title('A98N+W Sector Deprojected Profile Compared to P07 Universal')
    plt.ylabel('T[keV]')
    plt.xlabel('r/r$_{200}$')
    plt.legend()
    plt.savefig('a98nSector.5.a98wSector.2.deproj.tempProf.compUniversal.png')
    plt.show()


#ghirardini+2019 universal temperature profile

    x = r/r500
    tmint0 = 0.5
    t0 = 1.21
    rcool = np.power(10.,-2.78)
    rt = 0.34
    acool = 1.03
    c2 = 0.27

    tofx = t500*t0*((tmint0+np.power(x/rcool,acool))/(1.+np.power(x/rcool,acool)))*(1./np.power(1.+np.power(x/rt,2),c2))


    plt.errorbar(sector01wR/r200,sector01wTdeproj,xerr=[[0.175/r200],[0.175/r200]],yerr=[[0.34],[0.35]],fmt='deeppink',marker='.')
    plt.errorbar(sector02wR/r200,sector02wTdeproj,xerr=[[0.26/r200],[0.26/r200]],yerr=[[1.07],[1.86]],fmt='deeppink',marker='.',label='a98w deproj')
    plt.errorbar(sector03wR/r200,sector03wT,xerr=[[0.22/r200],[0.22/r200]],yerr=[[0.33],[0.62]],fmt='deeppink',marker='.')
    plt.errorbar(sector01r/r200,sector01tdeproj,xerr=[[0.175/r200],[0.175/r200]],yerr=[[0.34],[0.35]],fmt='g.')
    plt.errorbar(sector02r/r200,sector02tdeproj,xerr=[[0.26/r200],[0.26/r200]],yerr=[[1.07],[1.86]],fmt='g.',label='a98n deproj')
    plt.errorbar(sector03r/r200,sector03t,xerr=[[0.22/r200],[0.22/r200]],yerr=[[0.33],[0.62]],fmt='g.')
    plt.plot(r/r200,tofx,label='Ghirardini+2019')
    plt.ylabel('T[keV]')
    plt.xlabel('r/r$_{200}$')
    plt.legend()
    plt.savefig('a98nSector.5.a98wSector.2.deproj.tempProf.compUniversalGhirardini2019.png')
    plt.show()











tempprofGxyCluster()
