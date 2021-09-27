from numpy import *                     #import de numpy
from scipy.signal import periodogram    #import du module signal de scipy
from pylab import *                     #import de matplotlib.pylab

Fe=45000                   #fréquence d'échantillonnage
D= 10                         #Durée du signal en seconde
t = arange(0, 0.005, 1/Fe)        #creation de la base temps avec numpy
f1= 2000                          #fréquence du signal S1
f2= 18000                         #fréquence du signal S2
f3 = 20000
f4 = 9000

# S1 et S2 et S=S1+S2
S1 = 2*sin(2*pi*f1*t)                  #creation d'une sinusoide de Fréquence f1
S2 = sin(2*pi*f2*t)
S3 = 2*sin(2*pi*f3*t)
S4 = 2*sin(2*pi*f4*t)
  #creation d'une sinusoide de Fréquence f2
S= S1+S2+S3+S4


#calcul de la transformée de Fourier avec la fonction periodogram

f,FFT = periodogram(S,Fe)                # f: vecteur des fréquences et FFT:la transformée de Fourier du signal S=S1=S2=S3=S4


# Affichage du signal------------------------------------------------'
fig=figure(0)
plot(t,S)                     #Affichage via la fonction plot de Matplotlib
xlabel('Temps (s)')          #définition de l'axe des abscisses
ylabel('Amplitude')          #définition de l'axe des ordonnées
plt.title ('Signal S=S1+S2+S3+S4',fontsize=14)
plt.grid()
show()                          #affichage des courbes


# Affichage du de la transformée de Fourier FFT du signal S=S1=S2=S3=S4-----------------

plot(f,FFT)                     #Affichage via la fonction plot de Matplotlib
xlabel('Fréquence (Hz)')        #définition de l'axe des abscisses
ylabel('Module')                #définition de l'axe des ordonnées
plt.xlim(0, 22000)
plt.grid()
plt.title ('Module de la Transformée de Fourier du signal S=S1+S2+S3+S4',fontsize=14)
show()
#Définir la fréquence de coupure fc filtre à 17500 Hz
#Définir la fréquence de coupure fb filtre à 18500 Hz
fc= 17500
fb = 18500
# On définit une variable qui reçoit le signal filtré de la même taille que la transfomrée de fourier(FFT)
FFT_filtre= FFT


#On réalise un filre passe bas comme suit:

for i in range(len(f)):
    if f [i] < fc: # on coupe toutes les fréquences < 17500 Hz
        FFT_filtre [i] = 0.0
for i in range(len(f)):
    if f [i] > fb: # on coupe toutes les fréquences > 18500 Hz
        FFT_filtre [i] = 0.0

#On calcul la transfomrée de Fourier inverse du signal après filtrage en utilsant la focntion ifft de Python
# la FFT inverse permet de revenir dans l'espace temporal (espace Fourier -> espace temps)
FFT_inverse = np.fft.ifft(FFT_filtre)

fig=figure(0)
plot(f,FFT_filtre)              #Affichage via la fonction plot de Matplotlib
xlabel('Fréquence (Hz)')        #définition de l'axe des abscisses
ylabel('Module')                #définition de l'axe des ordonnées
plt.xlim(0, 22000)
plt.grid()
plt.title ('Module de la Transformée de Fourier du signal filtré s(t)',fontsize=14)
show()

plot(FFT_inverse)               #Affichage via la fonction plot de Matplotlib

ylabel('Amplitude')                #définition de l'axe des ordonnées
plt.xlim(0, 110)
plt.grid()
plt.title ('Le signal obtenu après filtrage',fontsize=14)
show()