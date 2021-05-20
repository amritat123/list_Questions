chart_list=["a","n","t","a","a","T","n","n","a","x","r","g","a","x","a"]
a=[]
i=0
while i<len(chart_list):
    j=0
    e=[]
    count=1
    while j<len(chart_list[i]):
        if chart_list[i]==chart_list[j]:
            count+=1
        j+=1 
        e.append(chart_list[i])
        e.append(count)
    if e not in a:
        a.append(e)
    i+=1
print()  