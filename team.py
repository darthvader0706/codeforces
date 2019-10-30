n = int(input())
count,mainCount = 0,0
for i in range(n):
    x = [int(x) for x in input().split()]
    for i in x:
        if i==1:
            count+=1
    if count>=2:
        mainCount+=1
    count=0
print(mainCount)