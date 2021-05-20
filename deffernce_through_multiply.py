#multiple kerke deffernce niklao....
a=[1,2,43,5]
b=[2,3,5,6]
multi=1
multi_1=1
i=0
while i<len(a):
	multi=a[i]*multi
	multi_1=a[i]*multi_1
	if multi>multi_1:
		deff=multi-multi_1
	else:
		deff=multi_1-multi
	i+=1
print(multi)
print(multi_1)
print(deff)