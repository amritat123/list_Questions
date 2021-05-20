element=[23,14,56,12,19,9,15,25,31,42,43]
sum=0
s=0
i=0
while i<len(element):
    if element[i]%2==0:
        sum=sum+element[i]
    else:
        s=s+element[i]
    i+=1
print(sum,"is even")
print(s,"odd")