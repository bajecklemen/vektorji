# Vektorji
To sta modula za risanje vektorjev z mathplotlib in osnovne funkcije z vektorji.

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

## vektorji_2b
Še pride razlaga