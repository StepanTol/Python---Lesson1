'''Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю 
наблюдений за погодой. Они обратились к синоптикам, а те, в 
свою очередь, занялись исследованиями статистики за 
прошлые годы. Их интересует, сколько дней длилась самая 
длинная оттепель. Оттепелью они называют период, в 
который среднесуточная температура ежедневно превышала 
0 градусов Цельсия. Напишите программу, помогающую 
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2'''

'''N = int(input("Введите число: "))
days = 0
maxdays = 0
for i in range(N):
    t = int(input("Введите среднесуточную температуру дня: "))
    if t > 0:
        days += 1
        if days > maxdays:
            maxdays = days
    else:
        days = 0
if maxdays > 0:
    print(f'Столько дней была оттепель: {maxdays}')
else:
    print("Оттепели не было")'''


#Тоже самое решение, но без вложенного цикла

N = int(input("Введите число: "))
days = 0
maxdays = 0
for i in range(N):
    t = int(input("Введите среднесуточную температуру дня: "))
    if t > 0:
        days += 1
    else:
        days = 0
        continue
    maxdays = days
if maxdays > 0:
    print(f'Столько дней была оттепель: {maxdays}')
else:
    print("Оттепели не было")