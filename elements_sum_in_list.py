n=30
num=[10,11,12,13,14,17,18,19]
i=0
b=[]
while i<len(num):
	j=i
	a=[]
	while j<len(num):
		if num[i]+num[j]==n:
			a.append(num[i])
			a.append(num[j])
			b.append(a)
		j+=1
	i+=1
print(b)


