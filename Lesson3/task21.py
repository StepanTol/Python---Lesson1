'''Напишите программу для печати всех уникальных 
значений в словаре. 
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
":" S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально. 
Пользователь его не вводит'''

# в словаре находятся элементы элементы состоят из ключа и значения 

# Метод values выводит все вторые значения словаря 

'''lst_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
lst = []
for item in lst_1:
    for val in item.values():
        if val not in lst:
            lst.append(val)
print(lst_1)
print(lst)'''

# Метод keys выводит все первые значения словаря 

'''lst_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
lst = []
for item in lst_1:
    for val in item.keys():
        if val not in lst:
            lst.append(val)
print(lst_1)
print(lst)'''

# Метод items выводит всё в формате списка из кортежей

'''lst_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
lst = []
for item in lst_1:
    for val in item.items():
        if val not in lst:
            lst.append(val)
print(lst_1)
print(lst)'''

# Решение без метода values

'''lst_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
lst = []
for item in lst_1:
    for key in item:
        val = item[key]
        if val not in lst:
            lst.append(val)
print(lst_1)
print(lst)'''


# Решение через множество

lst_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
result = set()

for dct in lst_1:
    result.add(*dct.values())

print(result)