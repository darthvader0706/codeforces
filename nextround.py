n,k = [int(x) for x in input().split()]

li = [int(x) for x in input().split()]
count = 0
if li[0]==0:
    print(0)
else:
    key = li[k-1]
    for i in li:
        if i>=key and i!=0:
            count+=1
    print(count)
