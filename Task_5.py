my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
num = int(input('Введите число:'))
while num != -1:
    for new in range(len(my_list)):
        if my_list[new] == num:
            my_list.insert(new + 1, num)
            break
        elif my_list[0] < num:
            my_list.insert(0, num)
        elif my_list[-1] > num:
            my_list.append(num)
        elif my_list[new] > num and my_list[new + 1] < num:
            my_list.insert(new + 1, num)
            break
    print(f"Текущий рейтинг - {my_list}")
    num = int(input('Введите число:'))
