marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]]
sum=0
i=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        avg=sum/15
        j+=1
    i+=1
print(avg)
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]
k=0
while k<len(marks):
    l=0
    while l<len(marks[k]):
        sum=sum+marks[k][l]
        avg=sum/12
        l+=1
    k+=1
print(avg)
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
] 
m=0
while m<len(marks):
    n=0
    while n<len(marks[m]):
        sum=sum+marks[m][n]
        avg=sum/17
        n+=1
    m+=1
print(avg)