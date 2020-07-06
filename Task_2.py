name = input('Введите имя:  ')
surname = input('Введите фамилию: ')
year = int(input('введите возраст: '))
city = input('Введите город: ')
email = input('Введите email:')
telephone = input('Введите телефон: ')


def my_func(inp_name,
            inp_surname,
            inp_year,
            inp_city,
            inp_email,
            inp_telephone):
    print('Имя: ', inp_name,
          ',Фамилия:', inp_surname,
          ',Возраст: ', inp_year,
          ',Город: ', inp_city,
          ',Email: ', inp_email,
          ',Телефон: ', inp_telephone)


my_func(name, surname, year, city, email, telephone)
