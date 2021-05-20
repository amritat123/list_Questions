num=[7,6,5,9,2,1,10]
i=0
while i<len(num)-1:
    j=0
    while j<i:
        if num[i]<num[j]:
            num[i],num[j+0]=num[j],num[i]
        j+=1
    i+=1
print(num)