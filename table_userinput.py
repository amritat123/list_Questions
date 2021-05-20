num=int(input("enter the num"))
n=int(input("any number"))
i=1
while i<=num:
	j=1
	while j<=n:
		multi= i*j
		print(i,"*",j,"=",multi)
		j+=1
	print()
	i+=1