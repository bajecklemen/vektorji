# Vektorji
To sta modula za risanje vektorjev z mathplotlib in osnovne funkcije za delo z vektorji.
## vektorji
Vektor je predstavljen z n-terko (tuple) npr. `(1,0,2)`. Vektor si lahko predstavljamo kot krajevni vektor ali točko v prostoru.
```
FUNCTIONS
    dolzina(x)
        Dolžina vektorja
    
    kolinearne(X, Y, Z)
        Ali so točke kolinearne
    
    komplanarne(x, y, z, w)
        Funkcija preveri če so 4 točke komplanarne = ležijo v ravnini
    
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
		
	linkomb(a,b,c,x):
		funkcija vrne linearno kombinacijo oblike x=m*a+n*b+p*c, kjer so a, b in c bazni vektorji, x pa vektor, ki ga izražamo. funkcija je definirana kot linkomb(a,b,c,x)
```
## Risanje
Za delovanje je potreben modul matplotlib.
```
pip install matplotlib
```
Naredimo objekt Risba(n), parameter je velikost slike od -n do n po x, y in z. Default vrednost je 3
```
r = Risba(4)
```
Če želimo na sloko dodati bazne enotske vektorje x, y in z:
```
r.baza()
```
Definirajmo nekaj krajevnih vektorjev:
```
a = (1,2,3)
b = (-2,-1,3)
n = (-1,1,6)
```
Vektorje na sliko dodamo tako:
```
r.vektor(a,'a','green')
r.vektor(n,'n','black')
```
Drugi parameter je oznaka vektorja, ki se prikaže na sliki in ni obvezen
Tretji parameter je barva, ni obvezen, default je 'blue'
```
r.pvektor(a,b,'b','blue')
```
Metoda pvektor nariše vektor b premaknjen za vektor a
```
r.prikaži()
```

