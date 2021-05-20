a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
magic=[]
while i<len(a):
	j=0
	r_sum=0
	c_sum=0
	while j<len(a[i]):
		c_sum=c_sum+a[i][j]
		r_sum=r_sum+a[j][i]
		j+=1
	i+=1
	magic.append(c_sum)
	magic.append (r_sum)
#print(c_sum)
#print(r_sum)
k=0
d1=0
d2=0
while k<len(a):
		d1=d1+a[k][k]
		d2=d2+a[k][2-k]
		k=k+1
#print(d1)
#print(d2)
if d1==d2 and r_sum==15 and c_sum==15:
		print("magic square")
else:
	print("nhi hai")