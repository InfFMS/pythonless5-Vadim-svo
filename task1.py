# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
import random

N = int(input())
a = []

for i in range (N):
    b = random.randint(0, 1000)
    a.append(b)

print(a)
print(len(a))
print(a[-1])
print(a[::-1])

c = 0
for i in range (len(a)):
    if a[i] % 10 == (a[i] // 10) % 10 == a[i] // 100:
        c += 1
if c > 0:
    print('YES')
else:
    print('NO')

a.pop(-1)
a.pop(0)
print(a)