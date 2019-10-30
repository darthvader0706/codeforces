n = int(input())
s = set()
li = [int(x) for x in input().split()]

for i in li:
    s.add(i)
    while n in s:
        print(n,end=' ')
        n-=1
    print()