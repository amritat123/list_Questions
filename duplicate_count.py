char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
count=0
i=0
a=[]
while i<len(char_list):
	if char_list[i] not in a:
		a.append(char_list[i])
		count+=1
	i+=1
print(a)
print(count)