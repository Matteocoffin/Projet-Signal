import binascii
V = bin(int.from_bytes('ESCAPE'.encode(), 'big'))
V = V.replace('b','')
print("binaire:",V)
print('')
code = str(V)
taille = len(code)
ln = '01'
f = ''
i = 0
while taille > i:
    if code[i]== ln[0]:
        f = str(f +'01')
    if code[i]== ln[1]:
        f = str(f+'10')
    i = i+1
    if taille < i+1:
        print('manchester:',f)
