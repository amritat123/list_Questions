a=[80,34,50,70,80,20,100]
i=0
bubble=0
while i<len(a):
	j=0
	while j<len(a):
		if a[i]<a[j]:
			bubble=a[j]
			a[j]=a[i]
			a[i]=bubble
		j+=1
	i+=1
print(a)