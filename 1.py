import random
n=int(input('Введите число:'))
a=[]
for i in range(n):
    a.append(random.randint(-10,10))

#int(a)
neg=[]
zero=[]
pos=[]
for el in a:
    if el<0:
        neg.append(el)
    if el==0:
        zero.append(el)
    if el>0:
        pos.append(el)


print("Отрицательные числа")
print(neg)
print("Положительные числа")
print(pos)
print("Нули")
print(zero)