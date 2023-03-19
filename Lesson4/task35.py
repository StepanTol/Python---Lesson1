'''Напишите функцию, которая принимает одно число и 
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое 
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes'''


N = int(input("Введите число: "))

def prime(N):
    count = 0
    for i in range(1, N+1):
        if N%i == 0:
            count += 1
    if count > 2:
        print(f'число {N} не является простым')
    else:
        print(f'число {N} простое') 
    return (f'Количество делителей равно =  {count}')
print(prime(N))


# Другое решение
num = int(input("Введите число: "))

def prime(num):
    for i in range(2, num//2):
        if num%i == 0:
            return False
    return True
print(prime(num))