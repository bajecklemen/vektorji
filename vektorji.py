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



if __name__ == '__main__':
    print('Modul vektorji')
    
    
    
    
    
