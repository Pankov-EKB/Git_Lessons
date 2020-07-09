from itertools import count
from math import factorial

n = int(input('Введите число, факториал которого хотите получить: '))


def fact():
    for el in count(1):
        yield factorial(el)


gen = fact()
x = 0
for i in gen:
    if x < n:
        print(i)
        x += 1
    else:
        break