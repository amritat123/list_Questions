my_list=[1,2,1]
list_1=[]
i=1
while i<=len(my_list):
    list_1.append(my_list[-i])
    i+=1
if list_1==my_list:
    print("plaindrome number h")
else:
    print("plaindrome nhi h")