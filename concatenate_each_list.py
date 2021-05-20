list1 = ["Hello ", "take"]
list2 = ["Dear", "Sir"]
i=0
my_list=[]
while i<len(list1):
    list3=list1[i]+list2[i]
    my_list.append(list3[i])
    i+=1
print(my_list) 
