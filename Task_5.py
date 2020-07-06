def sum_of_numbers():
    result_sum = 0
    ex = False
    while not ex:
        numbers = input('Ведите числа через пробел или # для выхода: ').split()
        result = 0
        for el in range(len(numbers)):
            if numbers[el] == '#':
                ex = True
                break
            else:
                result = result + int(numbers[el])
        result_sum = result_sum + result
        print('Текущая сумма = ', result_sum)
    print('Итоговая сумма = ', result_sum)


sum_of_numbers()
