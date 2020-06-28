a = input('Введите число:')
print('Последовательность чисел:')
print(a)
b = 1
new = a
sum = int(a)
while b < int(a):
    new = new + a
    b = b + 1
    sum = sum + int(new)
    print(new)
print('Сумма всех чисел последовательности:',sum)