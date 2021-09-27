from math import *

C = 1
C = C*(10**-6)
F = int(input("Fréquence propre"))

L = (1/(((F*2*pi)**2)*C))
Q = F/1000
R = (sqrt(L/C))/Q
print('Le condensateur à pour valeur',C,' Henry')
print('La bobine à pour valeur', L,' Henry')
print('La résistance à pour valeur',R,' ohm')


