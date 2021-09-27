

f1= [2,1,3,0]
f2=['v','h','b','j']
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
print(f1)
print(f2)