from random import randint

player_name = 'чел'
player_level = 5
player_hp = 99 + player_level


enemy_name = 'анти чел'
enemy_level = 1
enemy_hp = 99 + player_level

print(player_name, 'Против', enemy_name, '!')
        
while True:
    player_attack = randint(0, 10) * player_level
    input('нажми Enter что бы бить ')
    enemy_hp -= player_attack
    print(player_name, 'ударил', enemy_name, 'на', player_attack, 'жизней')
    print('у', enemy_name, 'стало', enemy_hp, 'жизней')
    if player_hp <= 0:
        print(player_name, 'проиграл')
        break
    
    enemy_attack = randint(0, 10) * enemy_level
    player_hp -= enemy_attack
    print(enemy_name, 'ударил', player_name, 'на', enemy_attack, 'жизней')
    print('у', player_name, 'стало', player_hp, 'жизней')
    if enemy_hp <= 0:
        print(enemy_name, 'проиграл')
        break

print('БОЙ ОКОНЧЕН!')
