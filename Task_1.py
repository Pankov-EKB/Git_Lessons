def sal():
    try:
        time = float(input('Выработка в часах: '))
        salary = int(input('Ставка: '))
        bonus = int(input('Премия: '))
        res = time * salary + bonus
        print('Заработная плата сотрудника: ', res)
    except ValueError:
        return print('Введите число')
sal()