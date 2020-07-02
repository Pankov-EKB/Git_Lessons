month = int(input('Введите номер месяца:'))
season = ['зима', 'весна', 'лето', 'осень']
season_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
if month <= 2 or month == 12:
    print(season[0])
    print(season_dict.get(1))
elif month > 2 and month <= 5:
    print(season[1])
    print(season_dict.get(2))
elif month > 5 and month <= 8:
    print(season[2])
    print(season_dict.get(3))
elif month > 8 and month <= 11:
    print(season[3])
    print(season_dict.get(4))
