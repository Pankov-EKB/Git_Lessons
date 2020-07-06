x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))


def my_func(z, q):
    if y != 0:
        res = z / q
        print('Результат деления:', res)
    else:
        print('Делить на ноль нельзя')


my_func(x, y)
