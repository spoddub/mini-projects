from random import randint
print('Хотите бросить кубики?')
repeat = input().lower()
if repeat == 'да':
    print('Бросок кубиков...')
    print('Первый кубик показывает:', randint(1, 6))
    print('Второй кубик показывает:', randint(1, 6))
    print('Попытать удачу еще разок? (Введите "да" или "нет")')
repeat = input().lower()
