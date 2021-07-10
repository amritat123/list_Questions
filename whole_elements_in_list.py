list1=[1,2,3,4],[5,6,7,8],[9,10,11,12]
a=len(list1)
print(type(list1))
i=0
list2=[]
while i<a:
    j=0
    while j<len(list1[i]):
        list2.append(list1[i][j])
        j+=1
    i+=1
print(list2)