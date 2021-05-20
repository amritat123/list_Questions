list="deepti"
i=0
name=[]
while i<len(list):
	name.append(list[i])
	i+=1
print(name)
j=0
while j<len(name):
	if name[j]=="p":
		name.remove(name[j])
	j+=1
print(name)