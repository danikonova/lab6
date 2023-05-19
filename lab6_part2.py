'''
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
Составьте все различные дроби из чисел 3, 5, 7, 11, 13, 17.
вариант 21
'''
from fractions import Fraction
from itertools import combinations

numbers = [3, 5, 7, 11, 13, 17]
fractions = set()

#Генерация всех дробей и добавление их во множество fractions
for i in range(len(numbers)):
    for j in range(len(numbers)):
        fractions.add(Fraction(numbers[i], numbers[j]))
        fractions.add(Fraction(numbers[j], numbers[i]))
        fractions.add(Fraction(numbers[i], numbers[i]))
        fractions.add(Fraction(numbers[j], numbers[j]))

max_fractions = []
max_sum = 0

#Итерация по всем возможным комбинациям дробей из fractions
for a, b in combinations(fractions, 2):
    a_num, a_den = a.as_integer_ratio()                                   #получаем числитель и знаменатель первой дроби из комбинации.
    b_num, b_den = b.as_integer_ratio()                                   #получаем числитель и знаменатель второй дроби из комбинации.
    if ((a_num + b_num) % 2 == 0) and ((a_den + b_den) % 2 == 0):
        num_sum = int(str(a_num+b_num)[-1]) + int(str(a_den+b_den)[-1])   #складываем последние цифры суммы числителей и знаменателей.
        if num_sum % 5 == 0:
            if abs(num_sum) > abs(max_sum):
                max_sum = num_sum
                max_fractions = [(a, b)]
            elif abs(num_sum) == abs(max_sum):
                max_fractions.append((a, b))

#Вывод результата - максимальной суммы и пары дробей
print("Максимальная сумма по модулю 5:", abs(max_sum))
print("Пары дробей, дающих максимальную сумму по модулю 5:")
for fractions in max_fractions:
    print(fractions)

