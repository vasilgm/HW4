# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random
n = int (input ('Введите количество элементов первого набора -> '))
list_one = []
m= int (input ('Введите количество элементов второго набора -> '))
list_two = []
for i in range(n):
    list_one.append(random.randint(1,25))
    i+=1
print(list_one)
for j in range(m):
    list_two.append(random.randint(1,25))
    j+=1
print(list_two)

list_one = set(list_one)

list_two = set(list_two)

list_three = {}
list_three = list(list_one.intersection(list_two))
list_three.sort()
print(list_three)