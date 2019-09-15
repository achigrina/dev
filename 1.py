import random
n=int(input('Введите число:'))
a=[]
for i in range(n):
    a.append(random.randint(-10,10))

print(a)