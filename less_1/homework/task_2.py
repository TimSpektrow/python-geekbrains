"""
2) Пользователь вводит время в секундах.
    Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
    Используйте форматирование строк.
"""

s = int(input("Введите количество секунд: "))

hour = s // (3600)
s %= (3600)
minute = s // 60
minute = str(f'0{minute}') if minute < 10 else minute

s %= 60
s = str(f'0{s}') if s < 10 else s

print(f"{hour}:{minute}:{s}")