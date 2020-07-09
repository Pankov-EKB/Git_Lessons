my_list = [5, 2, 2, 4, 3, 2, 1, 12, 8, 6, 6, 11, 3]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print('Элементы списка без повторений:', my_new_list)