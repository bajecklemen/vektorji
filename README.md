# Vektorji
To sta modula za risanje vektorjev z mathplotlib in osnovne funkcije z vektorji.
## vektorji

Vektor je predstavljen z n-terko (tuple) npr. `(1,0,2)`. Vektor si lahko predstavljamo kot krajevni vektor ali točko v prostoru.
Opis modula:
```
NAME
    vektorji

DESCRIPTION
    Funkcije za delo z vektorji
    Vektor je predstavljen z n-terko (tuple) npr. (1,0,2)
    Vektor je krajevni vektor ali točka v prostoru.

FUNCTIONS
    dolzina(x)
        Dolžina vektorja
    
    kot_med(x, y)
        Kot med vektorjema x in y
    
    mešani(x, y, z)
        Mešani produkt = volumen paralelpipeda
    
    nasprotni(x)
        Vrne nasprotni vektor
    
    razlika(x, y)
        Razlika dveh vektorjev x-y
        ali vektor od točke y do točke x
    
    skalarni(x, y)
        Skalarni produkt dveh vektorjev
    
    vektorski(x, y)
        Vektorski produkt
    
    vsota(x, y)
        Vrne vsoto dveh vektorjev
    
    vxs(x, s)
        vektor x krat skalar s
```

## Risanje

Za delovanje je potreben modul matplotlib.
```
pip install matplotlib
```
### Uporaba
```
#Naredimo objekt Risba, parameter je 
#velikost od -4 do 4 po x, y in z.
#default je 3
x = Risba(4)
#Nariše bazne vektorje x, y in z
x.baza()
#Nekaj vektorjev
a = (1,2,3)
b = (-2,-1,3)
n = (-1,1,6)
#Krajvni vektorji,
#ime in barvo lahko spustimo
x.vektor(a,'a','green')
x.vektor(n,'n','black')
#vektor se začne v točki a
x.pvektor(a,b,'b','blue')
x.prikaži()
```

