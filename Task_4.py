my_str = input('Введите строку из нескольких слов через пробел:')
list_my_str = []
b = 1
for el in range(my_str.count(' ') + 1):
    list_my_str = my_str.split()
    if len(str(list_my_str)) <= 10:
        print(f" {b} {list_my_str[el]}")
        b += 1
    else:
        print(f" {b} {list_my_str[el][0:10]}")
        b += 1
