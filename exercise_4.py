n = abs(int(input('Введите число:')))
max_num = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_num:
        max_num = n % 10
    if n > 9:
        continue
    else:
        print('Максимальная цифра в числе:', max_num)
        break
