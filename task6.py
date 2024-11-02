# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]

import random

N = int(input())
a = []
k = []
for i in range (N):
    b = random.randint(0, 1000)
    a.append(b)

print(a)

for i in range(len(a)//2):
    k.append(a[i])

a.reverse()
k.reverse()
a = [x for x in a if x not in k]

print(k+a)