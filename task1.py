'''За день машина проезжает n километров. Сколько 
дней нужно, чтобы проехать маршрут длиной m 
километров? При решении этой задачи нельзя 
пользоваться условной инструкцией if и циклами.'''

n = int(input("Введите кол-во км в день: "))
m = int(input("Введите расстояние: "))
a1 = m//n
a2 = int(bool(m%n))
result = a1 + a2
print(result)