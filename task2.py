'''Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |'''

N = int(input("Введите трёхзначное число: "))
a1 = N%10
a2 = (N//10)%10
a3 = N//100
result = a1 + a2 +a3
print(result)