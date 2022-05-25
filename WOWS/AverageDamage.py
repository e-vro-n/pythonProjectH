import sys

print("""Введите через пробел:
        КЛАСС корабля (k / l / e); УРОВЕНЬ корабля(8/9/10),
        текущий Средний урон; Кол-во боев, Ожидаемый урон... """)


def dmg100(dmg_my, battle, plan, clas,
           lvl):  # функция которая делает рассчет среднего урона(вставляем в функции классов кораблей)
    if battle > 99:
        prom_ave = dmg_my * battle
        btls = 0
        while (prom_ave / battle) < achive_info(clas, lvl):
            prom_ave += plan
            battle += 1
            btls += 1
            # return btls
        return f"необходимо сыграть {btls} боев при {plan} урона"
    else:
        new_avr = (dmg_my * battle + (100 - battle) * plan) / 100
        return f"{new_avr} - ср. урон при 100 боях (еще {str(100 - battle)} боев) при {plan} урона - (ачивка/" \
               f"{achive_info(clas, lvl)})!"


def ave_kr_100(dmg_my, battle, clas, lvl,
               plan):  # функция которая возвращает средний урон при плановом уроне при 100+ ббоях (clas, lvl, plan)
    if lvl == 8:
        return f"необходимо сыграть {dmg100(dmg_my, battle, plan, clas, lvl)} боев при {plan} урона"
    if lvl == 9:
        return f"необходимо сыграть {dmg100(dmg_my, battle, plan, clas, lvl)} боев при {plan} урона"


def ave_kr_50(dmg_my, battle, clas, lvl,
              plan):  # функция которая расчитывает ожидаемый средний урон при достижении 100 боев с заданным уроном
    if lvl == 9:
        new_avr = (dmg_my * battle + (100 - battle) * plan) / 100
        return f"{new_avr}- EstAvrDmg при 100 боях (еще {str(100 - battle)} боев) при {plan} урона - (ачивка/" \
               f"{achive_info(clas, lvl)})!"
    if lvl == 10:
        new_avr = (dmg_my * battle + (100 - battle) * plan) / 100
        return f"{new_avr} - ср. урон при 100 боях (еще {str(100 - battle)} боев) при {plan} урона - (ачивка/" \
               f"{achive_info(clas, lvl)})!"


def ave_lk_100(dmg_my, battle, clas, lvl, plan):
    if lvl == 8:
        c8 = 0
        prom_ave = dmg_my * battle
        while (prom_ave / battle) < achive_info(clas, lvl):
            prom_ave += plan
            battle += 1
            c8 += 1
        return f"необходимо сыграть {str(c8)} боев при {plan} урона"
    if lvl == 9:
        c8 = 0
        prom_ave = dmg_my * battle
        while (prom_ave / battle) < achive_info(clas, lvl):
            prom_ave += plan
            battle += 1
            c8 += 1
        return f"необходимо сыграть {str(c8)} боев при {plan} урона"


def ave_lk_50(dmg_my, battle, clas, lvl, plan):
    if lvl == 9:
        new_avr = (dmg_my * battle + (100 - battle) * plan) / 100
        return f"{new_avr}- EstAvrDmg при 100 боях (еще {str(100 - battle)} боев) при {plan} урона - (ачивка/" \
               f"{achive_info(clas, lvl)})!"
    if lvl == 10:
        new_avr = (dmg_my * battle + (100 - battle) * plan) / 100
        return f"{new_avr} - ср. урон при 100 боях (еще {str(100 - battle)} боев) при {plan} урона - (ачивка/" \
               f"{achive_info(clas, lvl)})!"


def ave_esm_100(dmg_my, battle, clas, lvl, plan):
    if lvl == 8:
        c8 = 0
        prom_ave = dmg_my * battle
        while (prom_ave / battle) < achive_info(clas, lvl):
            prom_ave += plan
            battle += 1
            c8 += 1
        return f"необходимо сыграть {str(c8)} боев при {plan} урона"
    if lvl == 9:
        c8 = 0
        prom_ave = dmg_my * battle
        while (prom_ave / battle) < achive_info(clas, lvl):
            prom_ave += plan
            battle += 1
            c8 += 1
        return f"необходимо сыграть {str(c8)} боев при {plan} урона"


def ave_esm_50(dmg_my, battle, clas, lvl, plan):
    if lvl == 8:
        new_avr = (dmg_my * battle + (100 - battle) * plan) / 100
        return f"{new_avr}- EstAvrDmg при 100 боях (еще {str(100 - battle)} боев) при {plan} урона - (ачивка/" \
               f"{achive_info(clas, lvl)})!"
    if lvl == 9:
        new_avr = (dmg_my * battle + (100 - battle) * plan) / 100
        return f"{new_avr}- EstAvrDmg при 100 боях (еще {str(100 - battle)} боев) при {plan} урона - (ачивка/" \
               f"{achive_info(clas, lvl)})!"
    if lvl == 10:
        new_avr = (dmg_my * battle + (100 - battle) * plan) / 100
        return f"{new_avr} - ср. урон при 100 боях (еще {str(100 - battle)} боев) при {plan} урона - (ачивка/" \
               f"{achive_info(clas, lvl)})!"


def achive_info(cls, lvl):  # функция с базовыми данными по урону на ачивку
    achive_data = {'k8': 55000, 'k9': 83000, 'k10': 0, 'l8': 72000, 'l9': 97000, 'l10': 0, 'e8': 40000, 'e9': 55000,
                   'e10': 0, 'к8': 55000, 'к9': 83000, 'к10': 0, 'л8': 72000, 'л9': 97000, 'л10': 0, 'э8': 40000,
                   'э9': 55000, 'э10': 0}
    return achive_data[f'{str(cls)}{str(lvl)}']

def check_input(dmg_my, battle, plan, clas, lvl):
    err = {}
    if dmg_my <= 0:
        err['(текущий ср.урон)'] = f'*!{dmg_my}!*'
    if battle <= 0:
        err['(екущий ср урон)'] = f'*!{battle}!*'
    if plan <= 0:
        err['(екущий ср урон)'] = f'*!{plan}!*'
    if lvl <= 0:
        err['(екущий ср урон)'] = f'*!{lvl}!*'
    if clas not in 'kleклэ':
        err['(екущий ср урон)'] = f'*!{clas}!*'
    if len(err) != 0:
        print(*err)
    if len(err) > 0:
        print('ok')



data = list(map(str.strip, sys.stdin))
rez_dic = {}
achive_dict = {}

for line in data:
    info = []
    clas, *info = line.split()
    info = list(map(int, info))
    # level, dmg, battles, plan = info
    lvl, dmg_my, battle, plan = info
    if (lvl or dmg_my or battle or plan) <= 0:
        print('Некорректный воод - отрицательные значения. Введите снова!')
        continue
    # print('level, dmg, battles, plan', level, dmg, battles, plan)
    if clas == 'k' or clas == 'к':
        rez_dic[f"Крейсера ({lvl})-го уровня"] = dmg100(dmg_my, battle, plan, clas, lvl)

        # if battles > 99:
        #     rez_dic[f"Крейсера ({level})-го уровня"] = ave_kr_100(dmg, battles, clas, level, plan)
        #     # print('рез_Кр', rez_dic)
        # else:
        #     rez_dic[f"Крейсера(less100) ({level})-го уровня"] = ave_kr_50(dmg, battles, clas, level, plan)

    # if clas == 'l' or clas == 'л':
    #     if battles > 99:
    #         rez_dic[f"Линкоры ({level})-го уровня"] = ave_lk_100(dmg, battles, clas, level, plan)
    #         # print('рез_Лк', rez_dic)
    #     else:
    #         rez_dic[f"Линкоры(less100) ({level})-го уровня"] = ave_lk_50(dmg, battles, clas, level, plan)
    # if clas == 'e' or clas == 'э':
    #     if battles > 99:
    #         rez_dic[f"Эсминцы ({level})-го уровня"] = ave_esm_100(dmg, battles, clas, level, plan)
    #         # print('рез_Эсм', rez_dic)
    #     else:
    #         rez_dic[f"Эсминцы(less100) ({level})-го уровня"] = ave_esm_50(dmg, battles, clas, level, plan)

print("Итого имеем:")
for key, value in rez_dic.items():
    print(f"{key} - {value}")
