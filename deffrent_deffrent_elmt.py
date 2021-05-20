row=int(input("any number"))
c=int(input("enter number"))
i=1
list1=[]
s=1
while i<=c:
	j=1
	b=s
	e=[]
	while j<=row:
		e.append(b)
		j+=1
		b+=1
	list1.append(e)
	i+=1
	s+=c
print(list1)