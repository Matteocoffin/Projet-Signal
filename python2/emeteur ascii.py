import binascii
import winsound

def bit():
    global parole,F
    F = bin(int.from_bytes(parole.encode(), 'big'))
    F = F.replace('b','')
    print("binaire:",F)



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



parole=input()
bit()
i=0
kseg=0
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