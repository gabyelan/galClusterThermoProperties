import math
import numpy as np
import matplotlib.pyplot as plt


def entropyProf():

#distances are in arcmin

    omegaM = 0.3
    omegaLambda = 0.7
    z=0.1042

    eofz = np.sqrt(omegaM*np.power(1.+z,3)+omegaLambda)

    print('eofz')
    print(eofz)

    ra98n = np.linspace(1,15,100)
    r200a98nArcmin = 10.4 #arcmin
    r500a98nArcmin = r200a98nArcmin/1.7
    r200a98n = r200a98nArcmin*60.*1.913/1.e3 #Mpc
    r500a98n = r500a98nArcmin*60.*1.913/1.e3
    t200a98n = 2.9

    ra98s = np.linspace(15,1,100)
    r200a98sArcmin = 10.9
    r500a98sArcmin = r200a98sArcmin/1.7
    r200a98s = r200a98nArcmin*60.*1.913/1.e3
    r500a98s = r500a98nArcmin*60.*1.913/1.e3
    t200a98s = 2.82

#voit+05

    k200a98n = 362.*t200a98n*np.power(eofz,-4./3.)
    
    k200a98s = 362.*t200a98s*np.power(eofz,-4./3.)
    
    r = np.linspace(0.15*r500a98n,1.4,100)

    ra98s = np.linspace(0.15*r500a98s,1.07,100)

    ka98n = 1.32*k200a98n*(r/r200a98n)**1.1

    ka98s = 1.32*k200a98s*(ra98s/r200a98s)**1.1

    ka98wSector3ssPredic = 1.32*k200a98n*(.3*r200a98n/r200a98n)**1.1

#a98nSector.5. deprojected; calculated with nhCalcGit.py

    kSector01 = 446.
    kSector02 = 1373.
    kSector03 = 781.

#a98wSector.2. deprojected

    kSector01w = 499.
    kSector02w = 1147.
    kSector03w = 848.

#a98nSector.5.

    kSector01proj = 435.
    kSector02proj = 1248.
    kSector03proj = 781.

#a98wSector.2.

    kSector01projW = 468.
    kSector02projW = 909.
    kSector03projW = 848.


#a98bridgewalk.3.

    k2halfBridgeBox = 501.
    k3bridgeBox = 610.
    k4bridgeBox = 807.
    k5bridgeBox = 627.
    k6bridgeBox = 588.
    k7bridgeBox = 537.

#a98bridgewalk.3. line of sight

    k2halfBridgeLOSCyl = 1783.
    k3BridgeLOSCyl = 2172.
    k4BridgeLOSCyl = 2871.
    k5BridgeLOSCyl = 2232.
    k6BridgeLOSCyl = 2091.
    k7BridgeLOSCyl = 2072.
    k8BridgeLOSCyl = 1840.

#a98bridgewalk.3.clyinder

    k2halfBridgeCyl = 463.
    k3bridgeCyl = 564.
    k4bridgeCyl = 745.
    k5bridgeCyl = 579.
    k6bridgeCyl = 542.
    k7bridgeCyl = 496.
    k8bridgeCyl = 477.

#a98nSector.5. [keV cm^2] entropy

    kSector01errLow = 51.
    kSector01errHigh = 51.
    kSector02errLow = 487.5
    kSector02errHigh = 781.
    kSector03errLow = 339.
    kSector03errHigh = 465.
    kSector01errLowProj = 45.
    kSector01errHighProj = 45.
    kSector02errLowProj = 414.
    kSector02errHighProj = 684.
    kSector03errLowProj = 339.
    kSector03errHighProj = 465.

#a98wSector.2. entropy errors [keV cm^2]

    kSector01errLowW = 73.
    kSector01errHighW = 86.
    kSector02errLowW = 354.
    kSector02errHighW = 492.
    kSector03errLowW = 552.
    kSector03errHighW = 663.
    kSector01errLowProjW = 56. 
    kSector01errHighProjW = 59.
    kSector02errLowProjW = 215.
    kSector02errHighProjW = 306.
    kSector03errLowProjW = 552.
    kSector03errHighProjW = 663.

#a98bridgewalk.3. errors

    k2halfBridgeBoxErrLow = 49.
    k2halfBridgeBoxErrHigh = 49.
    k3bridgeBoxErrLow = 74.
    k3bridgeBoxErrHigh = 74.
    k4bridgeBoxErrLow = 114.
    k4bridgeBoxErrHigh = 114.
    k5bridgeBoxErrLow = 113.
    k5bridgeBoxErrHigh = 113.
    k6bridgeBoxErrLow = 47.
    k6bridgeBoxErrHigh = 48.
    k7bridgeBoxErrLow = 60.
    k7bridgeBoxErrHigh = 60.


#a98bridgewalk.3.Cylinder errors

    k2halfBridgeCylErrLow = 45.
    k2halfBridgeCylErrHigh = 45.
    k3bridgeCylErrLow = 69.
    k3bridgeCylErrHigh = 69.
    k4bridgeCylErrLow = 105.
    k4bridgeCylErrHigh = 105.
    k5bridgeCylErrLow = 105.
    k5bridgeCylErrHigh = 105.
    k6bridgeCylErrLow = 43.
    k6bridgeCylErrHigh = 44.
    k7bridgeCylErrLow = 56.
    k7bridgeCylErrHigh = 56.
    k8bridgeCylErrLow = 77.
    k8bridgeCylErrHigh = 87.

#a98bridgewalk.3.Cylinder errors los

    k2halfBridgeCylLOSErrLow = 175.
    k2halfBridgeCylLOSErrHigh = 175.
    k3bridgeCylLOSErrLow = 265.
    k3bridgeCylLOSErrHigh = 265.
    k4bridgeCylLOSErrLow = 405.
    k4bridgeCylLOSErrHigh = 405.
    k5bridgeCylLOSErrLow = 403.
    k5bridgeCylLOSErrHigh = 403.
    k6bridgeCylLOSErrLow = 166.
    k6bridgeCylLOSErrHigh = 170.
    k7bridgeCylLOSErrLow = 232.
    k7bridgeCylLOSErrHigh = 232.  
    k8bridgeCylLOSErrLow = 299.
    k8bridgeCylLOSErrHigh = 336.

#a98nSector.5.

    sector01r = 0.275
    sector02r = 0.71
    sector03r = 1.19 #Mpc

#a98wSector.2.

    sector01rW = 0.275
    sector02rW = 0.71
    sector03rW = 1.19

#a98bridgewalk.3.A98N

    rBridge2half = 0.065
    rBridge3 = 0.24
    rBridge4 = 0.45
    rBridge5 = 0.685
    rBridge6 = 0.9
    rBridge7 = 1.05
    rBridge8 = 1.13

    rBridgetot = np.array([0.065,0.24,0.45,0.685,0.9,1.05,1.13])*(1.e3/(1.913*60.))

#a98bridgewalk.3.A98S

    rBridge2halfs = 1.05
    rBridge3s = 0.865
    rBridge4s = 0.645
    rBridge5s = 0.42
    rBridge6s = 0.2
    rBridge7s = 0.05

#a98nSector.5. bin sizes

    sector01rErrLow = 0.175 #Mpc (size of bins)
    sector01rErrHigh = 0.175
    sector02rErrLow = 0.26
    sector02rErrHigh = 0.26
    sector03rErrLow = 0.22
    sector03rErrHigh = 0.22
 
#a98wSector.2. bin sizes in [Mpc]

    sector01rErrLowW = 0.175
    sector01rErrHighW = 0.175
    sector02rErrLowW = 0.26
    sector02rErrHighW = 0.26
    sector03rErrLowW = 0.22
    sector03rErrHighW = 0.22

#a98bridgewalk.3.A98N bin sizes

    rBridgeErrLow = []
    rBridgeErrHigh = []

    rBridge2halfErrLow = 0.065
    rBridgeErrLow.append(rBridge2halfErrLow)
    rBridge2halfErrHigh = 0.065
    rBridgeErrHigh.append(rBridge2halfErrHigh)
    rBridge3ErrLow = 0.11
    rBridgeErrLow.append(rBridge3ErrLow)
    rBridge3ErrHigh = 0.11
    rBridgeErrHigh.append(rBridge3ErrHigh)
    rBridge4ErrLow = 0.11
    rBridgeErrLow.append(rBridge4ErrLow)
    rBridge4ErrHigh = 0.11
    rBridgeErrHigh.append(rBridge4ErrHigh)
    rBridge5ErrLow = 0.12
    rBridgeErrLow.append(rBridge5ErrLow)
    rBridge5ErrHigh = 0.12
    rBridgeErrHigh.append(rBridge5ErrHigh)
    rBridge6ErrLow = 0.1
    rBridgeErrLow.append(rBridge6ErrLow)
    rBridge6ErrHigh = 0.1
    rBridgeErrHigh.append(rBridge6ErrHigh)
    rBridge7ErrLow = 0.05
    rBridgeErrLow.append(rBridge7ErrLow)
    rBridge7ErrHigh = 0.05
    rBridgeErrHigh.append(rBridge7ErrHigh)
    rBridge8ErrLow = 0.08
    rBridgeErrLow.append(rBridge8ErrLow)
    rBridge8ErrHigh = 0.08
    rBridgeErrHigh.append(rBridge8ErrHigh)

    rBridgeErrLow = np.array(rBridgeErrLow)
    rBridgeErrHigh = np.array(rBridgeErrHigh)

    rBridgeErrLow = rBridgeErrLow*1.e3/(1.913*60.)
    rBridgeErrHigh = rBridgeErrHigh*1.e3/(1.913*60.)


#plots on plots on plots

#a98nSector.5. deprojected entropy profile

    plt.errorbar(sector01r/r200a98n,kSector01,yerr=[[kSector01errLow],[kSector01errHigh]],xerr=[[sector01rErrLow/r200a98n],[sector01rErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(sector02r/r200a98n,kSector02,yerr=[[kSector02errLow],[kSector02errHigh]],xerr=[[sector02rErrLow/r200a98n],[sector02rErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(sector03r/r200a98n,kSector03,yerr=[[kSector03errLow],[kSector03errHigh]],xerr=[[sector03rErrLow/r200a98n],[sector03rErrHigh/r200a98n]],fmt='k.')
    plt.plot(r/r200a98n,ka98n)
    plt.yscale('log')
    plt.ylabel('Entropy (Deporjected) [keV cm$^2$]')
    plt.xlabel('r/r200')
    plt.title('A98 N Sector Deprojected Entropy Profile')
    plt.savefig('a98nSector.5.entropyProfile.png')
    plt.show()

#a98nSector.5. and a98wSector.2. profiles in projection

    plt.errorbar(sector01r/r200a98n,kSector01proj,yerr=[[kSector01errLowProj],[kSector01errHighProj]],xerr=[[sector01rErrLow/r200a98n],[sector01rErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(sector02r/r200a98n,kSector02proj,yerr=[[kSector02errLowProj],[kSector02errHighProj]],xerr=[[sector02rErrLow/r200a98n],[sector02rErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(sector03r/r200a98n,kSector03proj,yerr=[[kSector03errLowProj],[kSector03errHighProj]],xerr=[[sector03rErrLow/r200a98n],[sector03rErrHigh/r200a98n]],fmt='k.',label='a98n')
    plt.errorbar(sector01rW/r200a98n,kSector01projW,yerr=[[kSector01errLowProjW],[kSector01errHighProjW]],xerr=[[sector01rErrLowW/r200a98n],[sector01rErrHighW/r200a98n]],fmt='deeppink',label='a98w')
    plt.errorbar(sector02rW/r200a98n,kSector02projW,yerr=[[kSector02errLowProjW],[kSector02errHighProjW]],xerr=[[sector02rErrLowW/r200a98n],[sector02rErrHighW/r200a98n]],fmt='deeppink')
    plt.errorbar(sector03rW/r200a98n,kSector02projW,yerr=[[kSector03errLowProjW],[kSector03errHighProjW]],xerr=[[sector03rErrLowW/r200a98n],[sector03rErrHighW/r200a98n]],fmt='deeppink')
    plt.plot(r/r200a98n,ka98n)
    plt.yscale('log')
    plt.title('A98 N and A98 W Projected Entropy Profile')
    plt.ylabel('Projected Entropy [keV cm$^2$]')
    plt.xlabel('r/r200')
    plt.legend()
    plt.savefig('a98nSector.5.a98wSector.2.entropyProfile.proj.png')
    plt.show()

#a98nSector.5. and a98wSector.2. deprojected profiles

    plt.errorbar(sector01r/r200a98n,kSector01,yerr=[[kSector01errLow],[kSector01errHigh]],xerr=[[sector01rErrLow/r200a98n],[sector01rErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(sector02r/r200a98n,kSector02,yerr=[[kSector02errLow],[kSector02errHigh]],xerr=[[sector02rErrLow/r200a98n],[sector02rErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(sector03r/r200a98n,kSector03,yerr=[[kSector03errLow],[kSector03errHigh]],xerr=[[sector03rErrLow/r200a98n],[sector03rErrHigh/r200a98n]],fmt='k.',label='a98n')
    plt.errorbar(sector01rW/r200a98n,kSector01w,yerr=[[kSector01errLowW],[kSector01errHighW]],xerr=[[sector01rErrLowW/r200a98n],[sector01rErrHighW/r200a98n]],fmt='deeppink',marker='.',label='a98w')
    plt.errorbar(sector02rW/r200a98n,kSector02w,yerr=[[kSector02errLowW],[kSector02errHighW]],xerr=[[sector02rErrLowW/r200a98n],[sector02rErrHighW/r200a98n]],marker='.',fmt='deeppink')
    plt.errorbar(sector03rW/r200a98n,kSector03w,yerr=[[kSector03errLowW],[kSector03errHighW]],xerr=[[sector03rErrLowW/r200a98n],[sector03rErrHighW/r200a98n]],marker='.',fmt='deeppink')
    plt.plot(r/r200a98n,ka98n)
    plt.yscale('log')
#    plt.ylabel('Deprojected Entropy [keV cm$^2$]')
    plt.xlabel('r/r$_{200}$')
    plt.ylabel('K [keV cm$^2$]')
    plt.legend()
    plt.savefig('a98nSector.5.a98wSector.2.entropyProfile.deproj.notitle.png')
    plt.show()

#a98bridgewalk.3.2half->7

    plt.errorbar(rBridge2half/r200a98n,k2halfBridgeBox,yerr=[[k2halfBridgeBoxErrLow],[k2halfBridgeBoxErrHigh]],xerr=[[rBridge2halfErrLow/r200a98n],[rBridge2halfErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(rBridge3/r200a98n,k3bridgeBox,yerr=[[k3bridgeBoxErrLow],[k3bridgeBoxErrHigh]],xerr=[[rBridge3ErrLow/r200a98n],[rBridge3ErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(rBridge4/r200a98n,k4bridgeBox,yerr=[[k4bridgeBoxErrLow],[k4bridgeBoxErrHigh]],xerr=[[rBridge4ErrLow/r200a98n],[rBridge4ErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(rBridge5/r200a98n,k5bridgeBox,yerr=[[k5bridgeBoxErrLow],[k5bridgeBoxErrHigh]],xerr=[[rBridge5ErrLow/r200a98n],[rBridge5ErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(rBridge6/r200a98n,k6bridgeBox,yerr=[[k6bridgeBoxErrLow],[k6bridgeBoxErrHigh]],xerr=[[rBridge6ErrLow/r200a98n],[rBridge6ErrHigh/r200a98n]],fmt='k.')
    plt.errorbar(rBridge7/r200a98n,k7bridgeBox,yerr=[[k7bridgeBoxErrLow],[k7bridgeBoxErrHigh]],xerr=[[rBridge7ErrLow/r200a98n],[rBridge7ErrHigh/r200a98n]],fmt='k.',label='box')
    plt.errorbar(rBridge2half/r200a98n,k2halfBridgeCyl,yerr=[[k2halfBridgeCylErrLow],[k2halfBridgeCylErrHigh]],xerr=[[rBridge2halfErrLow/r200a98n],[rBridge2halfErrHigh/r200a98n]],fmt='deeppink')
    plt.errorbar(rBridge3/r200a98n,k3bridgeCyl,yerr=[[k3bridgeCylErrLow],[k3bridgeCylErrHigh]],xerr=[[rBridge3ErrLow/r200a98n],[rBridge3ErrHigh/r200a98n]],fmt='deeppink')
    plt.errorbar(rBridge4/r200a98n,k4bridgeCyl,yerr=[[k4bridgeCylErrLow],[k4bridgeCylErrHigh]],xerr=[[rBridge4ErrLow/r200a98n],[rBridge4ErrHigh/r200a98n]],fmt='deeppink')
    plt.errorbar(rBridge5/r200a98n,k5bridgeCyl,yerr=[[k5bridgeCylErrLow],[k5bridgeCylErrHigh]],xerr=[[rBridge5ErrLow/r200a98n],[rBridge5ErrHigh/r200a98n]],fmt='deeppink')
    plt.errorbar(rBridge6/r200a98n,k6bridgeCyl,yerr=[[k6bridgeCylErrLow],[k6bridgeCylErrHigh]],xerr=[[rBridge6ErrLow/r200a98n],[rBridge6ErrHigh/r200a98n]],fmt='deeppink')
    plt.errorbar(rBridge7/r200a98n,k7bridgeCyl,yerr=[[k7bridgeCylErrLow],[k7bridgeCylErrHigh]],xerr=[[rBridge7ErrLow/r200a98n],[rBridge7ErrHigh/r200a98n]],fmt='deeppink',label='cylinder')
    plt.plot(r/r200a98n,ka98n)
    plt.yscale('log')
    plt.title('a98BridgeWalk.A98N')
    plt.ylabel('Projected Entropy [keV cm$^2$]')
    plt.xlabel('r/r$_{200}$')
    plt.legend()
    plt.savefig('a98bridgeWalk.2half.7.box.cylinder.comp.entropy.A98N.png')
    plt.show()

    plt.errorbar(rBridge2halfs/r200a98s,k2halfBridgeBox,yerr=[[k2halfBridgeBoxErrLow],[k2halfBridgeBoxErrHigh]],xerr=[[rBridge2halfErrLow/r200a98s],[rBridge2halfErrHigh/r200a98s]],fmt='k.',label='box')
    plt.errorbar(rBridge3s/r200a98s,k3bridgeBox,yerr=[[k3bridgeBoxErrLow],[k3bridgeBoxErrHigh]],xerr=[[rBridge3ErrLow/r200a98s],[rBridge3ErrHigh/r200a98s]],fmt='k.')
    plt.errorbar(rBridge4s/r200a98s,k4bridgeBox,yerr=[[k4bridgeBoxErrLow],[k4bridgeBoxErrHigh]],xerr=[[rBridge4ErrLow/r200a98s],[rBridge4ErrHigh/r200a98s]],fmt='k.')
    plt.errorbar(rBridge5s/r200a98s,k5bridgeBox,yerr=[[k5bridgeBoxErrLow],[k5bridgeBoxErrHigh]],xerr=[[rBridge5ErrLow/r200a98s],[rBridge5ErrHigh/r200a98s]],fmt='k.')
    plt.errorbar(rBridge6s/r200a98s,k6bridgeBox,yerr=[[k6bridgeBoxErrLow],[k6bridgeBoxErrHigh]],xerr=[[rBridge6ErrLow/r200a98s],[rBridge6ErrHigh/r200a98s]],fmt='k.')
    plt.errorbar(rBridge7s/r200a98s,k7bridgeBox,yerr=[[k7bridgeBoxErrLow],[k7bridgeBoxErrHigh]],xerr=[[rBridge7ErrLow/r200a98s],[rBridge7ErrHigh/r200a98s]],fmt='k.')
    plt.errorbar(rBridge2halfs/r200a98s,k2halfBridgeCyl,yerr=[[k2halfBridgeCylErrLow],[k2halfBridgeCylErrHigh]],xerr=[[rBridge2halfErrLow/r200a98s],[rBridge2halfErrHigh/r200a98s]],fmt='deeppink')
    plt.errorbar(rBridge3s/r200a98s,k3bridgeCyl,yerr=[[k3bridgeCylErrLow],[k3bridgeCylErrHigh]],xerr=[[rBridge3ErrLow/r200a98s],[rBridge3ErrHigh/r200a98s]],fmt='deeppink',label='cylinder')
    plt.errorbar(rBridge4s/r200a98s,k4bridgeCyl,yerr=[[k4bridgeCylErrLow],[k4bridgeCylErrHigh]],xerr=[[rBridge4ErrLow/r200a98s],[rBridge4ErrHigh/r200a98s]],fmt='deeppink')
    plt.errorbar(rBridge5s/r200a98s,k5bridgeCyl,yerr=[[k5bridgeCylErrLow],[k5bridgeCylErrHigh]],xerr=[[rBridge5ErrLow/r200a98s],[rBridge5ErrHigh/r200a98s]],fmt='deeppink')
    plt.errorbar(rBridge6s/r200a98s,k6bridgeCyl,yerr=[[k6bridgeCylErrLow],[k6bridgeCylErrHigh]],xerr=[[rBridge6ErrLow/r200a98s],[rBridge6ErrHigh/r200a98s]],fmt='deeppink')
    plt.errorbar(rBridge7s/r200a98s,k7bridgeCyl,yerr=[[k7bridgeCylErrLow],[k7bridgeCylErrHigh]],xerr=[[rBridge7ErrLow/r200a98s],[rBridge7ErrHigh/r200a98s]],fmt='deeppink')
    plt.plot(r/r200a98s,ka98s,'g')
    plt.yscale('log')
    plt.title('a98BridgeWalk.A98S')
    plt.ylabel('Projected Entropy [keV cm$^2$]')
    plt.xlabel('r/r$_{200}$')
    plt.legend()
    plt.savefig('a98bridgeWalk.2half.7.box.cylinder.comp.entropy.A98S.png')
    plt.show()
 
#los vs. plane of sky comp

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.errorbar(rBridge2half/r200a98n,k2halfBridgeCyl,yerr=[[k2halfBridgeCylErrLow],[k2halfBridgeCylErrHigh]],xerr=[[rBridge2halfErrLow/r200a98n],[rBridge2halfErrHigh/r200a98n]],fmt='deeppink')
    ax1.errorbar(rBridge3/r200a98n,k3bridgeCyl,yerr=[[k3bridgeCylErrLow],[k3bridgeCylErrHigh]],xerr=[[rBridge3ErrLow/r200a98n],[rBridge3ErrHigh/r200a98n]],fmt='deeppink')
    ax1.errorbar(rBridge4/r200a98n,k4bridgeCyl,yerr=[[k4bridgeCylErrLow],[k4bridgeCylErrHigh]],xerr=[[rBridge4ErrLow/r200a98n],[rBridge4ErrHigh/r200a98n]],fmt='deeppink')
    ax1.errorbar(rBridge5/r200a98n,k5bridgeCyl,yerr=[[k5bridgeCylErrLow],[k5bridgeCylErrHigh]],xerr=[[rBridge5ErrLow/r200a98n],[rBridge5ErrHigh/r200a98n]],fmt='deeppink')
    ax1.errorbar(rBridge6/r200a98n,k6bridgeCyl,yerr=[[k6bridgeCylErrLow],[k6bridgeCylErrHigh]],xerr=[[rBridge6ErrLow/r200a98n],[rBridge6ErrHigh/r200a98n]],fmt='deeppink')
    ax1.errorbar(rBridge7/r200a98n,k7bridgeCyl,yerr=[[k7bridgeCylErrLow],[k7bridgeCylErrHigh]],xerr=[[rBridge7ErrLow/r200a98n],[rBridge7ErrHigh/r200a98n]],fmt='deeppink',label='plane')
    ax1.errorbar(rBridge2half/r200a98n,k2halfBridgeLOSCyl,yerr=[[k2halfBridgeCylLOSErrLow],[k2halfBridgeCylLOSErrHigh]],xerr=[[rBridge2halfErrLow/r200a98n],[rBridge2halfErrHigh/r200a98n]],fmt='g^')
    ax1.errorbar(rBridge3/r200a98n,k3BridgeLOSCyl,yerr=[[k3bridgeCylLOSErrLow],[k3bridgeCylLOSErrHigh]],xerr=[[rBridge3ErrLow/r200a98n],[rBridge3ErrHigh/r200a98n]],fmt='g^')
    ax1.errorbar(rBridge4/r200a98n,k4BridgeLOSCyl,yerr=[[k4bridgeCylLOSErrLow],[k4bridgeCylLOSErrHigh]],xerr=[[rBridge4ErrLow/r200a98n],[rBridge4ErrHigh/r200a98n]],fmt='g^')
    ax1.errorbar(rBridge5/r200a98n,k5BridgeLOSCyl,yerr=[[k5bridgeCylLOSErrLow],[k5bridgeCylLOSErrHigh]],xerr=[[rBridge5ErrLow/r200a98n],[rBridge5ErrHigh/r200a98n]],fmt='g^')
    ax1.errorbar(rBridge6/r200a98n,k6BridgeLOSCyl,yerr=[[k6bridgeCylLOSErrLow],[k6bridgeCylLOSErrHigh]],xerr=[[rBridge6ErrLow/r200a98n],[rBridge6ErrHigh/r200a98n]],fmt='g^')
    ax1.errorbar(rBridge7/r200a98n,k7BridgeLOSCyl,yerr=[[k7bridgeCylLOSErrLow],[k7bridgeCylLOSErrHigh]],xerr=[[rBridge7ErrLow/r200a98n],[rBridge7ErrHigh/r200a98n]],fmt='g^',label='los')
    ax1.axvline(x = (1.056/r200a98n), color = 'indigo',linestyle = '--')
    ax1.plot(r/r200a98n,ka98n)
    ax1.set_yscale('log')
    ax1.set_ylabel('Projected Entropy [keV cm$^2$]')
    ax1.set_xlabel('r/r$_{200}$A98N')
    ax2.errorbar(rBridge2halfs/r200a98s,k2halfBridgeCyl,yerr=[[k2halfBridgeCylErrLow],[k2halfBridgeCylErrHigh]],xerr=[[rBridge2halfErrLow/r200a98s],[rBridge2halfErrHigh/r200a98s]],fmt='deeppink')
    ax2.errorbar(rBridge3s/r200a98s,k3bridgeCyl,yerr=[[k3bridgeCylErrLow],[k3bridgeCylErrHigh]],xerr=[[rBridge3ErrLow/r200a98s],[rBridge3ErrHigh/r200a98s]],fmt='deeppink')
    ax2.errorbar(rBridge4s/r200a98s,k4bridgeCyl,yerr=[[k4bridgeCylErrLow],[k4bridgeCylErrHigh]],xerr=[[rBridge4ErrLow/r200a98s],[rBridge4ErrHigh/r200a98s]],fmt='deeppink')
    ax2.errorbar(rBridge5s/r200a98s,k5bridgeCyl,yerr=[[k5bridgeCylErrLow],[k5bridgeCylErrHigh]],xerr=[[rBridge5ErrLow/r200a98s],[rBridge5ErrHigh/r200a98s]],fmt='deeppink')
    ax2.errorbar(rBridge6s/r200a98s,k6bridgeCyl,yerr=[[k6bridgeCylErrLow],[k6bridgeCylErrHigh]],xerr=[[rBridge6ErrLow/r200a98s],[rBridge6ErrHigh/r200a98s]],fmt='deeppink')
    ax2.errorbar(rBridge7s/r200a98s,k7bridgeCyl,yerr=[[k7bridgeCylErrLow],[k7bridgeCylErrHigh]],xerr=[[rBridge7ErrLow/r200a98s],[rBridge7ErrHigh/r200a98s]],fmt='deeppink',label='plane')
    ax2.errorbar(rBridge2halfs/r200a98s,k2halfBridgeLOSCyl,yerr=[[k2halfBridgeCylLOSErrLow],[k2halfBridgeCylLOSErrHigh]],xerr=[[rBridge2halfErrLow/r200a98s],[rBridge2halfErrHigh/r200a98s]],fmt='g^')
    ax2.errorbar(rBridge3s/r200a98s,k3BridgeLOSCyl,yerr=[[k3bridgeCylLOSErrLow],[k3bridgeCylLOSErrHigh]],xerr=[[rBridge3ErrLow/r200a98s],[rBridge3ErrHigh/r200a98s]],fmt='g^')
    ax2.errorbar(rBridge4s/r200a98s,k4BridgeLOSCyl,yerr=[[k4bridgeCylLOSErrLow],[k4bridgeCylLOSErrHigh]],xerr=[[rBridge4ErrLow/r200a98s],[rBridge4ErrHigh/r200a98s]],fmt='g^')
    ax2.errorbar(rBridge5s/r200a98s,k5BridgeLOSCyl,yerr=[[k5bridgeCylLOSErrLow],[k5bridgeCylLOSErrHigh]],xerr=[[rBridge5ErrLow/r200a98s],[rBridge5ErrHigh/r200a98s]],fmt='g^')
    ax2.errorbar(rBridge6s/r200a98s,k6BridgeLOSCyl,yerr=[[k6bridgeCylLOSErrLow],[k6bridgeCylLOSErrHigh]],xerr=[[rBridge6ErrLow/r200a98s],[rBridge6ErrHigh/r200a98s]],fmt='g^')
    ax2.errorbar(rBridge7s/r200a98s,k7BridgeLOSCyl,yerr=[[k7bridgeCylLOSErrLow],[k7bridgeCylLOSErrHigh]],xerr=[[rBridge7ErrLow/r200a98s],[rBridge7ErrHigh/r200a98s]],fmt='g^',label='los')
    ax2.axvline(x = (1.056/r200a98s), color = 'goldenrod',linestyle = '--')
    ax2.plot(r/r200a98s,ka98s,'k')
    ax2.set_yscale('log')
    ax2.set_xlabel('r/r$_{200}$A98S')
    ax2.legend(loc=4)
    plt.savefig('a98bridgeWalk.2half.7.losPlane.cylinder.comp.entropy.A98N.png')
    plt.show()

    rn = np.array(r*1.e3/(1.913*60.))
    rs = np.array(np.flip(ra98s)*1.e3/(1.913*60.))

    plt.errorbar(rBridgetot[0],k2halfBridgeCyl,yerr=[[k2halfBridgeCylErrLow],[k2halfBridgeCylErrHigh]],xerr=[[rBridgeErrLow[0]],[rBridgeErrHigh[0]]],fmt='deeppink')
    plt.errorbar(rBridgetot[1],k3bridgeCyl,yerr=[[k3bridgeCylErrLow],[k3bridgeCylErrHigh]],xerr=[[rBridgeErrLow[1]],[rBridgeErrHigh[1]]],fmt='deeppink',label='pos')
    plt.errorbar(rBridgetot[2],k4bridgeCyl,yerr=[[k4bridgeCylErrLow],[k4bridgeCylErrHigh]],xerr=[[rBridgeErrLow[2]],[rBridgeErrHigh[2]]],fmt='deeppink')
    plt.errorbar(rBridgetot[3],k5bridgeCyl,yerr=[[k5bridgeCylErrLow],[k5bridgeCylErrHigh]],xerr=[[rBridgeErrLow[3]],[rBridgeErrHigh[3]]],fmt='deeppink')
    plt.errorbar(rBridgetot[4],k6bridgeCyl,yerr=[[k6bridgeCylErrLow],[k6bridgeCylErrHigh]],xerr=[[rBridgeErrLow[4]],[rBridgeErrHigh[4]]],fmt='deeppink')
    plt.errorbar(rBridgetot[5],k7bridgeCyl,yerr=[[k7bridgeCylErrLow],[k7bridgeCylErrHigh]],xerr=[[rBridgeErrLow[5]],[rBridgeErrHigh[5]]],fmt='deeppink')
    plt.errorbar(rBridgetot[0],k2halfBridgeLOSCyl,yerr=[[k2halfBridgeCylLOSErrLow],[k2halfBridgeCylLOSErrHigh]],xerr=[[rBridgeErrLow[0]],[rBridgeErrHigh[0]]],fmt='g^',label='los')
    plt.errorbar(rBridgetot[1],k3BridgeLOSCyl,yerr=[[k3bridgeCylLOSErrLow],[k3bridgeCylLOSErrHigh]],xerr=[[rBridgeErrLow[1]],[rBridgeErrHigh[1]]],fmt='g^')
    plt.errorbar(rBridgetot[2],k4BridgeLOSCyl,yerr=[[k4bridgeCylLOSErrLow],[k4bridgeCylLOSErrHigh]],xerr=[[rBridgeErrLow[2]],[rBridgeErrHigh[2]]],fmt='g^')
    plt.errorbar(rBridgetot[3],k5BridgeLOSCyl,yerr=[[k5bridgeCylLOSErrLow],[k5bridgeCylLOSErrHigh]],xerr=[[rBridgeErrLow[3]],[rBridgeErrHigh[3]]],fmt='g^')
    plt.errorbar(rBridgetot[4],k6BridgeLOSCyl,yerr=[[k6bridgeCylLOSErrLow],[k6bridgeCylLOSErrHigh]],xerr=[[rBridgeErrLow[4]],[rBridgeErrHigh[4]]],fmt='g^')
    plt.errorbar(rBridgetot[5],k7BridgeLOSCyl,yerr=[[k7bridgeCylLOSErrLow],[k7bridgeCylLOSErrHigh]],xerr=[[rBridgeErrLow[5]],[rBridgeErrHigh[5]]],fmt='g^')
    plt.plot(rn[0:50],ka98s[0:50],'b',label='A98S ss')
    plt.plot(rs[0:50],ka98n[0:50],'k',label='A98N ss')
    plt.plot(rn[51:],ka98s[51:],'b--',)
    plt.plot(rs[51:],ka98n[51:],'k--')
    plt.yscale('log')
    plt.ylabel('Projected Entropy [keV cm$^2$]')
    plt.xlabel('r [arcmin]')
    plt.legend()
    plt.savefig('a98bridgeWalk.2half.7.box.cylinder.comp.entropy.A98SA98N.png')
#    plt.show()

entropyProf()
