list1 = ["Hello ", "take"]
list2 = ["Dear", "Sir"]
i=0
my_list=[]
while i<len(list2):
    j=0
    while j<len(list1):
        list3=list1[i]+list2[j]
        my_list.append(list3)
        j+=1
    i+=1
print(my_list)


