test = int(input())
for i in range(test):
    flag=1
    n=input()
    while(flag):
        if(n == n[::-1]):
            print(n)
            flag=0
        else:
            n = str(int(n)+1)