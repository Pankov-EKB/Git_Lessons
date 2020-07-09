my_list = [34, 345, 45, 6, 78, 98, 12, 43, 43, 4, 4, 6]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print('Исходный список: ', my_list)
print('Новый список: ', my_new_list)