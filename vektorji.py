'''
Funkcije za delo z vektorji
Vektor je predstavljen z n-terko (tuple) npr. (1,0,2)
Vektor je krajevni vektor ali točka v prostoru.
'''
import math

def nasprotni(x):
    '''Vrne nasprotni vektor'''
    return (-x[0],-x[1], -x[2])

def vsota(x,y):
    '''Vrne vsoto dveh vektorjev'''
    return (x[0]+y[0],x[1]+y[1],x[2]+y[2])

def razlika(x,y):
    '''
    Razlika dveh vektorjev x-y
    ali vektor od točke y do točke x
    '''
    return vsota(x,nasprotni(y))

def skalarni(x,y):
    '''
    Skalarni produkt dveh vektorjev
    '''
    return x[0]*y[0]+x[1]*y[1]+x[2]*y[2]

def dolzina(x):
    '''Dolžina vektorja'''
    return math.sqrt(skalarni(x,x))

def vxs(x,s):
    '''vektor x krat skalar s'''
    return (x[0]*s,x[1]*s,x[2]*s)

def kot_med(x,y):
    '''Kot med vektorjema x in y'''
    return math.degrees(math.acos(skalarni(x,y)/(dolzina(x)*dolzina(y))))

def vektorski(x,y):
    '''Vektorski produkt'''
    kx = x[1]*y[2] - x[2]*y[1]
    ky = x[2]*y[0] - x[0]*y[2]
    kz = x[0]*y[1] - x[1]*y[0]
    return (kx, ky, kz)
def mešani(x,y,z):
    '''Mešani produkt = volumen paralelpipeda'''
    return skalarni(x, vektorski(y,z))

def kolinearne(X,Y,Z):
    '''Ali so točke kolinearne'''
    return vektorski(razlika(Y, X), razlika(Z, X)) == (0, 0, 0)

def komplanarne(x,y,z,w):
    '''Funkcija preveri če so 4 točke komplanarne = ležijo v ravnini'''
    return mešani(razlika(y,x), razlika(y,z), razlika(y,w))==0   

def linkomb(a,b,c,x):
    '''funkcija vrne linearno kombinacijo oblike x=m*a+n*b+p*c, kjer so a, b in c bazni vektorji, x pa vektor, ki ga izražamo. funkcija je definirana kot linkomb(a,b,c,x)'''
    # k=((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))
    #predpostavimo, da c1=/=0 in b2*c1=/=c2*b1
    try:
        #abc
        m=(x[0]-(c[0]/c[1])*x[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*x[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*x[1])/(a[0]-(c[0]/c[1])*a[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*a[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*a[1])
        n=(x[2]-(c[2]/c[1])*x[1]-m*a[2]+(c[2]/c[1])*m*a[1])/(b[2]-(c[2]/c[1])*b[1])
        p=(x[1]-m*a[1]-n*b[1])/c[1]
        return (round(m,4),round(n,4),round(p,4))
    except:
        try:
            #acb
            d=b
            b=c
            c=d
            m=(x[0]-(c[0]/c[1])*x[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*x[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*x[1])/(a[0]-(c[0]/c[1])*a[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*a[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*a[1])
            n=(x[2]-(c[2]/c[1])*x[1]-m*a[2]+(c[2]/c[1])*m*a[1])/(b[2]-(c[2]/c[1])*b[1])
            p=(x[1]-m*a[1]-n*b[1])/c[1]
            return (round(m,4),round(p,4),round(n,4))
        except:
            try:
                #cab (zdj je bil og b preimenovan v c in og c preimenovan v b, zato menjam a in b (v resnici a in c))
                d=b
                b=a
                a=d
                m=(x[0]-(c[0]/c[1])*x[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*x[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*x[1])/(a[0]-(c[0]/c[1])*a[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*a[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*a[1])
                n=(x[2]-(c[2]/c[1])*x[1]-m*a[2]+(c[2]/c[1])*m*a[1])/(b[2]-(c[2]/c[1])*b[1])
                p=(x[1]-m*a[1]-n*b[1])/c[1]
                return (round(n,4),round(m,4),round(n,4))
            except:
                try:
                    #cba (zdj je a v c, b v a in c v b)
                    d=c
                    c=b
                    b=d
                    m=(x[0]-(c[0]/c[1])*x[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*x[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*x[1])/(a[0]-(c[0]/c[1])*a[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*a[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*a[1])
                    n=(x[2]-(c[2]/c[1])*x[1]-m*a[2]+(c[2]/c[1])*m*a[1])/(b[2]-(c[2]/c[1])*b[1])
                    p=(x[1]-m*a[1]-n*b[1])/c[1]
                    return (round(p,4),round(n,4),round(m,4))
                except:
                    try:
                        #bca (zdj je a v c, b v b in c v a)
                        d=a
                        a=b
                        b=d
                        m=(x[0]-(c[0]/c[1])*x[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*x[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*x[1])/(a[0]-(c[0]/c[1])*a[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*a[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*a[1])
                        n=(x[2]-(c[2]/c[1])*x[1]-m*a[2]+(c[2]/c[1])*m*a[1])/(b[2]-(c[2]/c[1])*b[1])
                        p=(x[1]-m*a[1]-n*b[1])/c[1]
                        return (round(n,4),round(p,4),round(m,4))
                    except:
                        try:
                            #bac (zdj je a v b, b v c in c v a)
                            d=b
                            b=c
                            c=d
                            m=(x[0]-(c[0]/c[1])*x[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*x[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*x[1])/(a[0]-(c[0]/c[1])*a[1]-((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*a[2]+((b[0]-(c[0]/c[1])*b[1])/(b[2]-(c[2]/c[1])*b[1]))*(c[2]/c[1])*a[1])
                            n=(x[2]-(c[2]/c[1])*x[1]-m*a[2]+(c[2]/c[1])*m*a[1])/(b[2]-(c[2]/c[1])*b[1])
                            p=(x[1]-m*a[1]-n*b[1])/c[1]
                            return (round(n,4),round(m,4),round(p,4))
                        except:
                            print('to ni mogoce - preveri, ali sta katera izmed baznih vektorjev kolinearna, ali pa je kakšen enak nicelnemu vektorju', a, b, c)
def det(M):
    '''Vrne determinantto matrike 3x3'''
    a = M[0][0]*M[1][1]*M[2][2]
    b = M[0][1]*M[1][2]*M[2][0]
    c = M[1][0]*M[2][1]*M[0][2]
    d = M[0][2]*M[1][1]*M[2][0]
    e = M[0][1]*M[1][0]*M[2][2]
    f = M[0][0]*M[1][2]*M[2][1]
    return a+b+c-d-e-f

def lin_komb(a,b,c,x):
    '''funkcija vrne linearno kombinacijo oblike x=m*a+n*b+p*c'''
    D = det((a,b,c))
    if D == 0:
        return None
    else:
        return (det((x,b,c))/D, det((a,x,c))/D, det((a,b,x))/D)

if __name__ == '__main__':
    print('Modul vektorji')
    
    
    
    
    
    
