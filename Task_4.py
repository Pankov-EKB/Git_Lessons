class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернул(а) направо'

    def turn_left(self):
        return f'{self.name} повернул(а) налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} = {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины  {self.name} = {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной для городского автомобиля'
        else:
            return f'Скорость {self.name} нормальная для городской машины'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} = {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной для рабочего автомобиля'
        else:
            return f'Скорость {self.name} нормальная для рабочей машины'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

porsche = SportCar(120, 'Красный', 'Porsche', True)
kia = TownCar(50, 'Синий', 'Kia', False)
kamaz = WorkCar(70, 'Оранжевый', 'Kamaz', False)
ford = PoliceCar(110, 'Белый',  'Ford', True)
print(kamaz.turn_left())
print(f'Когда {kia.turn_right()}, потом {porsche.stop()}')
print(f'{kamaz.go()} со скоростью {kamaz.show_speed()}')
print(f'{kamaz.name} - {kamaz.color}')
print(f' {porsche.name} полицейская машина? {porsche.is_police}')
print(f' {kamaz.name}  полицейская машина? {kamaz.is_police}')
print(porsche.show_speed())
print(kia.show_speed())
