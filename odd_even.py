element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
while i<len(element): 
    if element[i]%2==0:
        print(element[i],"even")
    else:
        print(element[i],"is odd")
    i+=1