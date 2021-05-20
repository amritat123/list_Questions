n=[50,40,23,70,56,12,5,10,7]
i=0
max=0
sec=0
while i<len(n):
	if n[i]>max:
		sec=max
		max=n[i]
	if sec<n[i]and n[i]<max:
		sec=n[i]
	i=i+1
print(sec)