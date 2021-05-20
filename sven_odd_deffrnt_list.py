a=[]
i=1
while i<=101:
    a.append(i)
    i+=1
# print(a)
b=[]
c=[]
j=0
while j<len(a):
    if a[j]%2==0:
        b.append(a[j])
    else:
        c.append(a[j])
    j+=1
print(b,"Even")
print(c,"Odd")