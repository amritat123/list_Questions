num=int(input("enter any num="))
num1=int(input("enter nay num="))
i=0
list=[]
while i<num:
    j=0
    list1=[]
    while j<num1:
        n=int(input("enter any num="))
        list1.append(n)
        j+=1
    list.append(list1)
    i+=1
print(list)