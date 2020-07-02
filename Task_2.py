a = int(input("Введите количество элементов списка: "))
my_list = []
b = 0
el_list = 0
while b < a:
    my_list.append(input("Введите следующее значение списка: "))
    b += 1
print(my_list)
for elem in range(int(len(my_list) / 2)):
    my_list[el_list], my_list[el_list + 1] = my_list[el_list + 1], my_list[el_list]
    el_list += 2
print(my_list)
