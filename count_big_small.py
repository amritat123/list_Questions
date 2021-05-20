list=[50,40,23,70,56,25,38,12,5,10,7]
count=0
n=len(list)
i=0
while i<n:
	if list[i]>20 and list[i]<40:
		count=count+1
	i=i+1
print(count)