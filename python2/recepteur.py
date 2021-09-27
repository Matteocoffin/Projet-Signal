import binascii

tramelettre= ['']*5
tramenumeror= ['']*5
test=['0110100101100110','011010010101100101101001010110','0110101001011010','011010010101100101101001010101','0110100101011010','0110100101010101011010010101100101101001010110','0110100101010110','01101001010101010110100101011001011010010101010101101001010110','0110101001010101','01101001010101010110100101011001011010010101010101101001010101','0110101001010101','01101001010101010110100101011001011010010101010101101001010101']
trame=['01010101011001010110011010011001010101011010','01010101011001101001011010010101010101011010','01010101011001100110100110010101010101011010','01010101011001010110100101101001010101011010','01010101011001101010010101011001010101011010']
code=['']*len(trame)


def manchesterlettre(n):
    global frank
    i = 0
    code = n
    taille = len(code)
    ln = '0110'
    v=''

    while taille > i:
        if code[i:i+2]== ln[0:2]:
            v = str(v +'0')
        if code[i:i+2]== ln[2:4]:
            v = str(v+'1')
        i = i+2
        if taille < i+1:
            frank=binascii.unhexlify('%x' % int('0b' + v, 2))

def manchesternumero(n):
    global franki
    i = 0
    code = n
    taille = len(code)
    ln = '0110'
    v=''

    while taille > i:
        if code[i:i+2]== ln[0:2]:
            v = str(v +'0')
        if code[i:i+2]== ln[2:4]:
            v = str(v+'1')
        i = i+2
        if taille < i+1:
            franki=v
def supprime():
    global code
    i=0
    while i < len(code):
      text=''
      text=code[i]
      text=text.replace(text[0:7],'')
      text=text.replace(text[len(text)-7:len(text)],'')
      code[i]=text
      i=i+1

def hammingsup():
    global code
    i=0
    l=0
    while i < len(code):
      témoin=''
      text=''
      text=code[i]
      if i == 0:
        témoin = text[2]+text[4]+text[6]+text[i]

      if i == 1:
        témoin = text[2]+text[5]+text[6]+text[i]

      if i == 3:
        témoin = text[4]+text[5]+text[6]+text[i]
        l=1

      B=témoin.count('1')
      if int(B)%2 == 1:
             print('erreur')
      text=text.replace(text[0:2],'',1)
      text = text.replace(text[1],'',1)
      code[i]=text
      i=i+1
def paire():
    global code
    i=0
    k=0
    v=''
    while len(code)>i:
        tab=['']*len(code[i])
        x= code[i].count('1')
        if x%2 == 0:
            text=code[i]
            while len(code[i]) > k:
                 tab[k]= text[k]
                 k=k+1
            del tab[k-1]
            k=0
            while len(tab)>k:
                v = v + tab[k]
                k=k+1
            k=0
            code[i]=v
            v=''
        else:
            print('erreur')
        i = i+1

def traducteur():
    global tramelettre,tramenumeror,code
    lettre=''
    numero=''
    mot=''
    k=0
    while len(tramenumeror)>k:
                numero = numero + str(tramenumeror[k])
                numero=numero.replace('b','')
                numero=numero.replace("'",'')
                tramenumeror[k] = numero
                numero=''
                k=k+1
    k=0
    while len(code)>k:
                mot = mot + str(code[k])
                k=k+1

    k=1
    v=''
    i=0
    i1 = 0
    i2=0
    print(tramenumeror)
    while i2!= 100:
        if mot[i1:k] == tramenumeror[i]:
            v = v + str(tramelettre[i])
            i1 = i1 + (len(mot[i1:k]))
            i = -1
        if len(tramelettre)-1 == i:
            k=k+1
            i=-1
        if k == len(mot)+1:
            i2 = 100
        i=i+1
    v=v.replace('b','')
    v=v.replace("'",'')
    print(v)



i = 0
k=0
while i < len(tramelettre)*2:
    manchesterlettre(test[i])
    tramelettre[k]=frank
    i = i+1
    manchesterlettre(test[i])
    tramenumeror[k]=frank
    i=i+1
    k=k+1

print(tramelettre)
print(tramenumeror)
i=0

while i < len(trame):
    manchesternumero(trame[i])
    code[i]=franki
    i = i+1

print(code)
supprime()
print(code)
print()
print("vérification du bit de parité")
paire()
print(code)
print()
print("vérification de hamming")
hammingsup()
print(code)
print()
print("traduction escape avec bibliothèque")
traducteur()
input()


