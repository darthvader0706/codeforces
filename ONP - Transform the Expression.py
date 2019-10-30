signs = {'+':1,
        '-':2,
        '*':3,
        '/':4,
        '^':5
        }
testcases= int(input())
for i in range(testcases):
    expression =input()
    stack=[]
    for i in expression:
        if i=='(':
            stack.append(i)
        if i==')':
            j=len(stack)-1
            while(stack[j]!='('):
                print(stack.pop(),end="")
                j-=1
            stack.pop()
        if i.isalnum():
            print(i,end="")
        if i in signs:
            if len(stack)!=0:
                while((stack[len(stack)-1] in signs) and (signs[stack[len(stack)-1]] > signs[i])):
                    print("Entered")
                    print(stack.pop(),end="")
                stack.append(i)
            else:
                stack.append(i)
    if(len(stack)!=0):
        for i in stack:
            print(i,end="")
    stack=[]
    print('\n')