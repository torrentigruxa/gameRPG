from helpers import *
from data import *

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Информаиция об игроке
5 - Показать инвентарь
6 - Магазин
7 - Завод
''')
    if action == '1':
        value=random.random()
        for i,elem in  enumerate(distribution):
            if value<elem:
                current_enemy=i
                break
        current_enemy = fight(current_enemy)
    elif action == '2':
        training_type = input('''1 - тренировать атаку
2 - тренировать оборону
''')
        training(training_type)
    elif action == '3':
        display_player()
        print()
    elif action == '5':
        display_inventory()
        print()
    elif action == '6':
        shop()
        print()
    elif action == '7':
        earn()
        print()
    print()




