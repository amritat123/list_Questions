num=[50,40,23,70,56,12,5,10,7]
i=0
min=num[0]
while i<len(num):
	if num[i]<min:
		min=num[i]
	i=i+1
print(min)