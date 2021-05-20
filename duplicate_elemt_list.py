a=[1,1,2,3,4,3,5,4]
i=0
j=[]
while i<len(a):
	if  a[i] not in j:
		j.append (a[i])
	i+=1
print(j)