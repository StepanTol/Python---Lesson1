'''Дана последовательность из N целых чисел и число 
K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – 
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]'''

k = int(input("Введите число: "))
List_1 = [1, 2, 3, 4, 5]
lst = []
#for i in range(5):
#    n = int(input("Введите элемент списка: "))
#    List_1.append(n)
print(List_1)
for i in range(len(List_1)):
    if i+k < len(List_1):
        lst.append(List_1[i+k])
    else:
        lst.append(List_1[i+k-len(List_1)])
print(lst)