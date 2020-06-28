a = int(input("Введите результаты пробежки первого дня в км: "))
b = int(input("Введите общий желаемый результат в км: "))
result_days = 1
result_km = a
print('Результат:')
print(f"{result_days}день:{a} км")
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
        print(f'{result_days} день:'"%.2f" %a,"км")
print(f'Ответ: На {result_days} день спортсмен достигнет общего результата бега {b} км.')