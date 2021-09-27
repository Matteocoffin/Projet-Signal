import binascii
import winsound

def dicodet():
 global f1,f2,r,c,f,ft,fc,F,parole
 a=parole
 a1=parole
 c=0
 ft=0
 fc=0
 r=0
 test = len(a)
 f1=[0]*test
 f2=['']*test
 i = 0
 f={}
 def teur(k):
    global f1,c,f2,r
    compteur=0
    for i in a:
       if i==a[k]:
          compteur+=1
    if compteur >= 2:
          r = r+compteur
    f1[c] = compteur
    f2[c] = a[k]


 def croix():
    global f1,f2
    i = 0
    av=0
    ap=0
    av1=''
    ap1=''
    k=1
    while i < len(f1):
        if i == len(f1)-1:
            k=0
        if i < 0:
            i = 0
        if f1[i] < f1[i+k]:
            av = f1[i]
            ap = f1[i+1]
            av1=f2[i]
            ap1=f2[i+1]
            f2[i]=ap1
            f2[i+1]=av1
            f1[i]=ap
            f1[i+1]=av
            i=i-2
        i=i+1




 def classeur():
    global f1,ft,fc
    croix()
    k1=0
    k2 = len(f1)
    i=len(f1)
    k=1
    d=0
    n=1
    ft=''
    fc=''
    if len(f1) == 1:
        ft=[1]
        n=0
    while sum(f1[k1:k])+(sum(f1[i:k2])*n) != sum(f1):
        i=i-1
        ft=f1[k1:k]
        fc=f1[i:k2]
        if sum(f1[k1:k]) == sum(f1[i:k2]) and sum(f1[k1:k])+sum(f1[i:k2]) != sum(f1):
            k = k+1
            i=len(f1)-1
        if sum(f1[k1:k]) < sum(f1[i:k2]) and sum(f1[k1:k])+sum(f1[i:k2]) != sum(f1):
            k = k+1
            i=len(f1)-1


 def dico():
    global ft,fc,f2,f
    p=0
    p1 = 0
    i = 0
    k=0
    k1=0
    i1 = 0
    ftest = ft
    fctest = fc
    couche = 1
    while p != 100:
       if couche == 1:
                f[f2[i]]= f[f2[i]]+'1'
                if i == int(len(ft)-1):
                    couche = 2
                i=i+1
       if couche == 2:
                f[f2[i]]= f[f2[i]]+'0'
                if i == len(f2)-1:
                    couche = 3
                i=i+1

       if couche == 3:
            while int(len(ftest)/2) != int(len(ftest[k1:k])):
                    print(k)
                    f[f2[k]]= f[f2[k]]+'1'
                    k=k+1
            while int(len(ftest)) != int(len(ftest[k1:k])):
                    f[f2[k]]= f[f2[k]]+'0'
                    k=k+1
            re=0
            while re < k:
                if re != k:
                    ftest[re] = f[f2[re]]
                    x = ftest.count(str(f[f2[k-1]]))

                re = re+1
            if len(f2) <= 1:
                k=0
                i = 0
                couche = 3
            if x > 1:
                del f2[0]
                del ftest[0]
                k=0
                i = 0
                couche = 3
            if x <= 1:
                couche = 4
                del f1[0:len(ft)]
                del f2[0:len(ft)]
                p = 100
    k=0
    i=0
    req = 0
    x=0
    while p1 != 100:
        if req == 0:
         if couche == 4:
                f[f2[i]]= f[f2[i]]+'1'
                if i == len(fc)-1:
                    couche = 5
                i=i+1
        if couche == 5:
            while int(len(fctest)/2) != int(len(fctest[k1:k])):
                   f[f2[k]]= f[f2[k]]+'1'
                   k=k+1
            while int(len(fctest)) != int(len(fctest[k1:k])):
                  f[f2[k]]= f[f2[k]]+'0'
                  k=k+1
            re=0
            while re < k:
                if re != k:
                   fctest[re] = f[f2[re]]
                   x = fctest.count(str(f[f2[k-1]]))

                re = re+1
            if len(f2) <= 1:
                k=0
                i = 0
                couche = 5
            if x > 1:
                del f2[0]
                del fctest[0]
                k=0
                i = 0
                couche = 5
            if x <= 1:
                couche = 4
                del f1[0:len(fc)]
                del f2[0:len(fc)]
                p1 = 100

 m=0

 while len(a) != 0 :
    teur(0)
    a = a.replace(a[0],'')
    m = m+1
    c = c + 1

 while i != len(f2)-1:
    f[f2[i]]=''
    i = i+1
 while 0 in f1:
    del f1[f1.index(0)]

 while '' in f2:
    del f2[f2.index('')]
 h=0
 while len(f2) > h:
    f[f2[h]]=''
    h=h+1

 classeur()
 croix()
 dico()


 i9 = 0
 F = ''
 k = 0
 for i in a1:
    if i == a1[k]:
        F = F + f[i]
    k=k+1

 print('le mot en binaire', F)


def encodage():
 global donnee,man
 code = str(donnee)
 taille = len(code)
 ln = '01'
 man = ''
 i = 0
 while taille > i:
    if code[i]== ln[0]:
        man = str(man +'01')
    if code[i]== ln[1]:
        man = str(man+'10')
    i = i+1
    if taille < i+1:
        print('manchester:',man)
        print()




def hamming():
 global seg,ham
 message = seg
 n=2
 k=0
 l = 2
 v = 0
 t=0
 test = 0
 go=[2]*(len(message)+1)
 mes=[0]*len(message)
 for i in message:
    if i==message[k]:
        mes[k] = message[k]
    k = k+1

 while v < len(message):
    if v <= 1:
        mes.insert(0,'k')
        go[v+1] = 0+t

    else:
        go[v+1] = n**l
        mes.insert(n**l-1,'k')
        l = l +1

    t=t+1
    v = v+1
 if mes[len(mes)-1]== 'k':
    del mes[len(mes)-1]
 parite=['']*3
 i=0
 while i < 10:
    if i == 0:
       témoin = mes[2]+mes[4]+mes[6]
       k = 11
       k2 = 1
    if i == 1:
       témoin = mes[2]+mes[5]+mes[6]
       k = 11
       k2 = 2
    if i == 2:
       témoin = mes[4]+mes[5]+mes[6]
       k = 11
       k2 = 3
    if k >= len(mes):
        k = 0
        parite[i]=témoin
        témoin=''
        i = k2
    if i == 3:
        i = 10

 i = 0
 while i != 3:
    B=parite[i].count('1')
    if B%2 == 0:
        parite[i]='0'
    if B%2 == 1:
        parite[i]='1'

    i = i+1
 mes[0]=parite[0]
 mes[1]=parite[1]
 mes[3]=parite[2]
 i = 0
 ham = ''
 while i < len(mes):
       ham = ham+mes[i]
       i=i+1


def segmentation():
    global F,seg,kseg
    req=0
    seg= ''
    seg=F[kseg:kseg+4]
    if len(seg) < 4:
        req = 4-len(seg)
        seg=seg+'0'*req
    kseg = kseg+4

    print(seg)

def tetetrame():
   global ham,donnee
   donnee=ham
   x = donnee.count('1')
   if x%2 == 0:
       donnee = donnee + '0'
   else:
        donnee = donnee + '1'
   donnee= '0000010'+donnee+'0000011'


def envoie():
    global man
    code = man
    i=0
    while i < len(code):
        if code[i] == '1':
            winsound.Beep(27000, 50)
        if code[i] == '0':
            winsound.Beep(25000, 50)
        i = i+1


def singaldico():
 global f
 i=0
 k=0
 tc=['']*len(f)
 tn=['']*len(f)
 for cle in f:
    tc[k]=cle
    tn[k]=f[cle]
    k = k+1
 while '' in tc and tn:
    del tc[tc.index('')]
    del tn[tn.index('')]
 i=0
 k=0
 while len(f) > k:
    i = 0
    fr=''
    v1=''
    v=''
    i1 = 0
    v1=bin(int.from_bytes(tc[k].encode(), 'big'))
    v=bin(int.from_bytes(tn[k].encode(), 'big'))
    while len(v1) > i:
        if v1[i]== '0':
              fr = str(fr +'01')
        if v1[i]== '1':
              fr = str(fr+'10')
        i = i+1
        if len(v1) < i+1:
              print()
              print('manchester:',fr,"lettre", tc[k])
              i1=0
              while i1 < len(fr):
                   if fr[i1] == '1':
                         winsound.Beep(22000, 50)
                   if fr[i1] == '0':
                         winsound.Beep(20000, 50)
                   i1 = i1+1
    i = 0
    fr=''
    while len(v) > i:
        if v[i]== '0':
              fr = str(fr +'01')
        if v[i]== '1':
              fr = str(fr+'10')
        i = i+1
        if len(v) < i+1:
              print('manchester:',fr,"de", tn[k])
              i1=0
              while i1 < len(fr):
                   if fr[i1] == '1':
                         winsound.Beep(22000, 50)
                   if fr[i1] == '0':
                         winsound.Beep(20000, 50)
                   i1 = i1+1
    k = k+1
parole=input()
dicodet()
i=0
kseg=0
print("envoie du dictionnaire")
singaldico()
print()
print('code avec segmentation en 4 bits')
print()
while (len(F)/4) > i:
    segmentation()
    hamming()
    tetetrame()
    encodage()
    envoie()
    i = i+1


input()

