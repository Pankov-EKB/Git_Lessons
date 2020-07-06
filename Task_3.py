arg_1 = int(input('Введите первый аргумент: '))
arg_2 = int(input('Введите второй аргумент: '))
arg_3 = int(input('Введите третий аргумент: '))
my_list = [arg_1, arg_2, arg_3]


def my_func(arg):
    m_1 = max(arg)
    arg.remove(m_1)
    m_2 = max(arg)
    my_sum = m_1 + m_2
    print('Сумма наибольших аргуметов: ', my_sum)


my_func(my_list)
