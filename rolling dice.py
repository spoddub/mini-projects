# импоритим из рандома функцию randint
from random import randint

# спрашиваем хочет ли пользователь бросить кубики в первый раз
print('Хотите бросить кубики?')
repeat = input().lower()


if repeat == 'да':
    print('Бросок кубиков...')
    print('Первый кубик показывает:', randint(1, 6))
    print('Второй кубик показывает:', randint(1, 6))
    print('Попытать удачу еще разок? (Введите "да" или "нет")')  # хочет ли пользователь сыграть еще раз?

repeat = input().lower()   # пользователь вводит свой ответ
