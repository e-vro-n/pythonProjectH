def print_hi(name):
    print(f'Hi, {name}')


# name = 'Lim'
name = 'll'
if name == 'Lim':
    print_hi('Hi')
else:
    print_hi(999)
    print("Nea")

a = '''k 8 52919 119 75000
k 9 71809 13 85000

k 8 53765 121 75000
k 9 74945 15 85000
l 8 70786 293 80000
l 9 74827 131 100000
e 8 38942 54 45000
e 9 36392 22 60000
'''

dmg_my = 52919
battle = 119
plan = 75000
clas = 'k'
lvl = 5


# lvl = 8
# if lvl == 8:
#     c8 = 0
#     prom_ave = dmg_my * battle
#     print('gg', prom_ave, 'avvvv', round(prom_ave / battle, 2))
#     # prom_ave = dmg_my * battle + plan
#     print('p', prom_ave)
#     while (prom_ave / battle) < 55000:
#         prom_ave += plan
#         # print('AW', round(prom_ave / battle, 1))
#         battle += 1
#         c8 += 1
#         print('prom', prom_ave, 'AW', round(prom_ave / battle, 1), 'bat', battle, 'c8', c8)

# проверка функций проверки ввода
def check_input(dmg_my, battle, plan, clas, lvl):
    err = {}
    if dmg_my <= 0:
        err['текущий ср.урон'] = f'{dmg_my}(!)'
    if battle <= 0:
        err['кол-во боев'] = f'{battle}(!)'
    if plan <= 0:
        err['план урона'] = f'{plan}(!)'
    if lvl <= 0:
        err['уровень корабля'] = f'{lvl}(!)'
    if (clas not in 'kleклэ') or clas == "":
        err['класс корабля'] = f'( {clas} )(!)'
    if len(err) != 0:
        print('!!! ОШИБКА ВВОДА :')
        for key, value in err.items():
            print(f'{key}: {value} ', end=':: ')
    if len(err) == 0:  # подумать -надо ли
        print('ok')


check_input(dmg_my, battle, plan, clas, lvl)
