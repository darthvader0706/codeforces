x = input()
vowels = 'aeiouy'
x = list(x.lower())
y=[]
# print(x)
for i in x:
    if i not in vowels:
        y.append(i)
for i in range(len(y)):
    y[i] = '.'+y[i]
print("".join(y))    
