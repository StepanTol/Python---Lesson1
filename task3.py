'''В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для 
них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в 
каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.'''

#1-й вариант решения

'''a = int(input("Введите кол-во учащихся в первом классе: "))
b = int(input("Введите кол-во учащихся во втором классе: "))
c = int(input("Введите кол-во учащихся в третьем классе: "))
a1 = a//2 + int(bool(a%2))
a2 = b//2 + int(bool(b%2))
a3 = c//2 + int(bool(c%2))
result = a1 + a2 + a3
print(result)'''

#2-й вариант решения

import math
a = int(input("Введите кол-во учащихся в первом классе: "))
b = int(input("Введите кол-во учащихся во втором классе: "))
c = int(input("Введите кол-во учащихся в третьем классе: "))
result = math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2) # math.ceil - округление результата в большую сторону
print (result)