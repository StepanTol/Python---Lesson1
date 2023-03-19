'''Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1'''

from random import randint
N = int(input("Введите количество оценок: "))      # lst = [randint(0, 5) for i in range(N)]
lst = []
for i in range(N):
    lst.append(randint(0,10))
print(lst)

max = max(lst)
min = min(lst)  # min/max - встроенные функции минимального и максимального значений

for i in range(N):       # Функция enumerate - возвращает кортеж из двух элементов - индекса и значения
    if lst[i] == max:    # Тогда можем переписать 19 и 20 строку
        lst[i] = min     # for i, val in enumerate(lst)
print(lst)               # if val == max


###########
'''from random import randint
N = int(input("Введите количество оценок: "))      # Можно вводить отметки самому:
lst = []                                           # Тогда: lst = [int(input()) for _ in range(5)]
for i in range(N):
    lst.append(randint(0,10))
print(lst)

x = min(lst)
y = max(lst)
lst_2 = [x if i == y else i for i in lst]
print(lst_2)'''