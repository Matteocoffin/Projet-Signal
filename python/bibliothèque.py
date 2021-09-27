a='escape'
a1='escape'
c=0
ft=0
fc=0
r=0
test = len(a)
délimiteur=0
f1=[0]*test
f2=['']*test
i = 0
f={}
dictionnaire={}
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

def décodeur ():
    global F,f
    decode = F
    i=0
    k=0
    tc=['']*len(decode)
    tn=['']*len(decode)
    for cle in f:
       tc[k]=cle
       tn[k]=f[cle]
       k = k+1
    while '' in tc and tn:
        del tc[tc.index('')]
        del tn[tn.index('')]
    k=1
    v=''
    i1 = 0
    i2=0
    while i2!= 100:
        if decode[i1:k] == str(tn[i]):
           v = v + tc[i]
           i1 = i1 + (len(decode[i1:k]))
           i = -1
        if len(tc)-1 == i:
           k=k+1
           i=-1
        if k == len(decode)+1:
           i2 = 100
        i=i+1

    print(v)

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
    global ft,fc,f2,f,dictionnaire
    p=0
    p1 = 0
    i = 0
    k=0
    k1=0
    i1 = 0
    ftest = ft
    fctest = fc
    couche = 1
    print(ft)
    print(fc)
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
i = 0
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
print(f)


i9 = 0
F = ''
k = 0
for i in a1:
    if i == a1[k]:
        F = F + f[i]
    k=k+1

print(F)

décodeur()







