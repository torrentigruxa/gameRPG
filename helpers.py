import random
import time
from data import *
def fight(current_enemy):
    round=random.randint(1,2)
    enemy=enemies[current_enemy]

    enemy_hp=enemies[current_enemy]['hp']
    print(f'Противник-{enemy["name"]}: {enemy["script"]}')
    input('Нажмите Enter чтобы продолжить.')

    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit=random.randint(1,100)
            if crit<player['luck']:
                enemy_hp -= player['attack']*3
            else:
                enemy_hp -= player['attack']
            time.sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            time.sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack']*player['armor']
            time.sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            time.sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy+=1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp']=100
    return current_enemy

def training(training_type):
    skip='2'
    if items['2']['name'] in player['inventory']:
        skip=input('Желаете пропустить тренеровку? 1. Да 2. Нет ')
    if skip == '2':
        for i in range(0,101,20):
            print(f'тренеровка завершена на {i}%')
            time.sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player['armor'] -= .09
        print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    print()

def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Веилична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')

def display_inventory():
    print('У вас есть ')
    for value in player['inventory']:
        print(value)
    print(f'У вас есть {player["money"]} монет')
    if 'Зелье удачи' in player['inventory']:
        potion=input('Желаете выпить зелье удачи? 1. Да 2. Нет')
        if potion== '1':
            player['luck']+=7
            player['inventory'].remove('Зелье удачи')
            print(f'Готово! Теперь шанс нанести критический урон равен {player["luck"]}%')
            
def shop():
    print('Добро пожаловать, путник! Что хочешь приобрести?')
    print(f'У тебя есть {player["money"]} монет.')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')

    item = input()
    if items[item]["name"] in player['inventory']:
        print(f'У тебя уже есть {items[item]["name"]}')
    elif player['money'] >= items[item]['price']:
        print(f'Ты успешно приобрёл {items[item]["name"]}')
        player['inventory'].append(items[item]["name"])
        player['money'] -= items[item]['price']
    else:
        print('Не хватает монет :(')
    print()
    print('Буду ждать тебя снова, путник!')
    print()

def earn():
    print('Добро пожаловать на завод! У вас есть 67% шанс заработать 500 монет и 33% потерять 500 монет')
    result = random.randint(1, 100)
    time.sleep(1.5)
    print('Результат....')
    time.sleep(1.5)
    print('Страшно?!')
    if result < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
    else:
        print('Вы проиграли 500 монет :(')
        player['money'] -= 500
    print()
    print(f'Осталось монет: {player["money"]}')
    print()