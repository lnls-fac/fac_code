
import numpy as _np
import math as _math
from scipy.integrate import quad


def Calc_Lifetime(param,I0,twiss,ex,ey,sigP,sigS):
# Dicionary param = basic machine parameters
    s=_np.zeros(len(twiss))
    betax=_np.zeros(len(twiss))
    alphax=_np.zeros(len(twiss))
    betay=_np.zeros(len(twiss))
    alphay=_np.zeros(len(twiss))
    Dx=_np.zeros(len(twiss))
    Dpx=_np.zeros(len(twiss))
    Dy=_np.zeros(len(twiss))
    Dpy=_np.zeros(len(twiss))
    accp=_np.zeros(len(twiss))
    accn=_np.zeros(len(twiss))

    s=twiss[:,0]
    #len=twiss[:,1]
    #mux=twiss[:,2]
    betax=twiss[:,3]
    alphax=twiss[:,4]
    Dx=twiss[:,5]
    Dpx=twiss[:,6]
    #muy=twiss[:,7]
    betay=twiss[:,8]
    alphay=twiss[:,9]
    Dy=twiss[:,10]
    Dpy=twiss[:,11]
    accp=twiss[:,12]
    accn=twiss[:,13]


    Ds=_np.zeros(len(twiss))
    acc=_np.zeros(len(twiss))

    Ds=s-_np.roll(s,1)
    Ds[0]=0
    acc=_np.minimum(accp,accn)
    betax_avg=_np.average(betax,weights=Ds)
    betay_avg=_np.average(betay,weights=Ds)
    #print "<betax> = ",betax_avg
    #print "<betay> = ",betay_avg
    #print "<acc> = ",_np.average(acc,weights=Ds)#, "<accp> = ",_np.average(accp,weights=Ds), "<accn> = ",_np.average(accn,weights=Ds)
    #Elastic Scattering Lifetime
    Telas=10.25*2.0*_math.pi/FR*(param['En']/1.0e+09)**2*param['Ay']/(betay_avg*Pmed)

    sigx=_np.zeros(len(twiss))
    sigy=_np.zeros(len(twiss))
    epsilon=_np.zeros(len(twiss))
    Tv=_np.zeros(len(twiss))
    dsdT=_np.zeros(len(twiss)-1)

    sigx=_np.sqrt(betax*ex+(Dx*sigP)**2)
    epsilonn=(accn)**2*(betax/ex)/(1957.0*param['En']/1.0e+09)**2
    Tvp=(5.39e17*(param['En']/1.0e+09)**2*(accp)**3*sigx*sigy*sigS/(De(epsilonp)*C))**(-1.0)
    Tvn=(5.39e17*(param['En']/1.0e+09)**2*(accn)**3*sigx*sigy*sigS/(De(epsilonn)*C))**(-1.0)
    aux=0.5*(_np.average(Tvp,weights=Ds)+_np.average(Tvn,weights=Ds))
    Ttous=1.0/(aux*I0)

def Calc_Lifetime_Matlab(Pmed,param,twiss,ex,ey,sigP,sigS):
# Dicionary param = basic machine parameters
    s=_np.zeros(len(twiss))
    betax=_np.zeros(len(twiss))
    alphax=_np.zeros(len(twiss))
    betay=_np.zeros(len(twiss))
    alphay=_np.zeros(len(twiss))
    Dx=_np.zeros(len(twiss))
    Dpx=_np.zeros(len(twiss))
    Dy=_np.zeros(len(twiss))
    Dpy=_np.zeros(len(twiss))
    accp=_np.zeros(len(twiss))
    accn=_np.zeros(len(twiss))

    # s=twiss[:,0]
    # betax=twiss[:,2]
    # alphax=twiss[:,3]
    # betay=twiss[:,6]
    # alphay=twiss[:,7]
    # Dx=twiss[:,4]
    # Dpx=twiss[:,5]
    # Dy=twiss[:,8]
    # Dpy=twiss[:,9]
    # accp=twiss[:,10]
    # accn=twiss[:,11]
    # Ds=_np.zeros(len(twiss))
    # acc=_np.zeros(len(twiss))

    s=twiss[:,0]
    #len=twiss[:,1]
    #mux=twiss[:,2]
    betax=twiss[:,3]
    alphax=twiss[:,4]
    Dx=twiss[:,5]
    Dpx=twiss[:,6]
    #muy=twiss[:,7]
    betay=twiss[:,8]
    alphay=twiss[:,9]
    Dy=twiss[:,10]
    Dpy=twiss[:,11]
    accp=twiss[:,12]
    accn=twiss[:,13]
    Ds=_np.zeros(len(twiss))
    acc=_np.zeros(len(twiss))

    Ds=s-_np.roll(s,1)
    Ds[0]=0
    acc=_np.minimum(accp,accn)
    betax_avg=_np.average(betax,weights=Ds)
    betay_avg=_np.average(betay,weights=Ds)
    #print "<betax> = ",betax_avg
    #print "<betay> = ",betay_avg
    #print "<acc> = ",_np.average(acc,weights=Ds)#, "<accp> = ",_np.average(accp,weights=Ds), "<accn> = ",_np.average(accn,weights=Ds)
    gamma=param['gamma']
    Np=param['Np']
    #Elastic Scattering Lifetime
    Telas=10.25*2.0*pi/FR*(param['En']/1.0e+09)**2*param['Ay']/(betay_avg*Pmed)

    sigx=_np.zeros(len(twiss))
    sigy=_np.zeros(len(twiss))
    epsilon=_np.zeros(len(twiss))
    Tv=_np.zeros(len(twiss))
    dsdT=_np.zeros(len(twiss)-1)

    #bunch size and volume
    sigx=_np.sqrt(betax*ex+(Dx*sigP)**2)
    V=sigS*sigx*sigy

    # parameters
    Sx2=ex*betax
    factor=betax*Dpx+alphax*Dx
    A1=1.0/(4.0*sigP**2)+(Dx**2+factor**2)/(4.0*Sx2)
    B1=betax*factor/(2.0*Sx2)
    C1=betax**2/(4.0*Sx2)-B1**2/(4.0*A1)
    #Epsilon factors
    #epsilonp=(2.0*_np.sqrt(C1)/gamma*accp)**2
    #epsilonn=(2.0*_np.sqrt(C1)/gamma*accn)**2
    epsilonp=(2.0*_np.sqrt(C1)*accp)**2/(1957.0*param['En']/1.0e+09)**2
    epsilonn=(2.0*_np.sqrt(C1)*accn)**2/(1957.0*param['En']/1.0e+09)**2


    #Lifetime
    Tvp=9.4718e-23*Np/(gamma**2)*1/(accp**3)*De(epsilonp)/V
    Tvn=9.4718e-23*Np/(gamma**2)*1/(accn**3)*De(epsilonn)/V
    aux=0.5*(_np.average(Tvp,weights=Ds)+_np.average(Tvn,weights=Ds))*3600
    Ttous=1.0/aux


    out=_np.zeros(len(e))
    for j in range(len(e)):
        out[j]=0.5*_math.sqrt(e[j])*(-3.0*_math.exp(-e[j])+e[j]*int1+int2*(3.0*e[j]-e[j]*_math.log(e[j])+2.0))