check = '1001'
modulo = 2**(len(check))
somme=0
k=0
for i in check:
    if i == '1':
       somme = somme + 2**k
    k = k+1

test = somme%modulo
i=0
r=0
f=0
v=''
test = bin(test)
test = test.replace(test[0:2],'')
while len(check) > i:
    if test[i]== '1':
        v = str(v +'0')
    if test[i]== '0':
        v = str(v+'1')
    i = i+1

print(v)