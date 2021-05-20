list=[59,40,70,56,10,12,7,2]
i=0
max=0
min=list[i]
while i<len(list):
		if list[i]>max:
			max=list[i]
		if list[i]<min:
			min=list[i]
		i=i+1
print(max)
print(min)