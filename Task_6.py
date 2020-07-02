goods = int(input("Сколько всего у вас товаров: "))
my_list = []
name = []
cost = []
count = []
unit = []
for i in range(goods):
    my_dict = dict({'название': input("Введите название: "), 'цена': input("Введите цену: "), 'количество': input("Введите количество: "), 'eд': input("Введите единицу измерения: ")})
    my_turple = (i+1, my_dict)
    my_list.append(my_turple)
    name.append(my_dict['название'])
    cost.append(my_dict['цена'])
    count.append(my_dict['количество'])
    unit.append(my_dict['eд'])
    my_analys = dict({'название': name, 'цена': cost, 'количество': count, 'eд': unit})
for item in my_list:
    print(item)
for item in my_analys.items():
    print(item)
