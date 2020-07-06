x = int(input('Введите положительное число: '))
y = int(input('Введите целое отрицательное число: '))


def my_func(a, b):
    res = 1 / (a ** abs(b))
    print('Результат,', a, 'в степени', b, '=', round(res, 3))


my_func(x, y)


def new_func(a, b):
    ans = 1
    b = abs(b)
    for i in range(b):
        ans = ans * 1 / a
    print('Результат,', a, 'в степени -', b, '=', round(ans, 3))


new_func(x, y)
