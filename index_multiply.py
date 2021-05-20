list=[[1,2,3],[4,5,6],[7,8,9]]
i=0
while i<len(list):
    j=0
    multi=1
    while j<len(list[i]):
       multi=list[j][i]*multi
       j+=1
    print(multi)
    i+=1