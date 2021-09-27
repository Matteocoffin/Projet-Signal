dico={}
dico['d']='010'
dico['m']='10'
dico['e']= '11'
dico['r']= '011'

decode = '101101101011'
i=0
k=0
tc=['']*len(decode)
tn=['']*len(decode)
for cle in dico:
    tc[k]=cle
    tn[k]=dico[cle]
    k = k+1
while '' in tc and tn:
    del tc[tc.index('')]
    del tn[tn.index('')]
k=1
v=''
i1 = 0
i2=0
print(tn)
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