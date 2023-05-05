'''
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
Найти все возможные пары чисел из списка, сумма которых равна 10, а разница между ними не превышает 2.Целевая функция: минимизация количества пар чисел, удовлетворяющих условиям.
Составьте все различные дроби из чисел 3, 5, 7, 11, 13, 17.
вариант 21
'''

#часть 2
numbers = [3, 5, 7, 11, 13, 17]
fractions = []

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        fractions.append(numbers[i]/numbers[j])
        fractions.append(numbers[j]/numbers[i])
print(fractions)


def find_pairs(numbers, target_sum, max_diff):        #перебор всех возможных пар чисел из списка numbers и проверка на удовлетворение условию задачи.
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum and abs(numbers[i] - numbers[j]) <= max_diff:
                pairs.append((numbers[i], numbers[j]))
    return pairs

def minimize_pairs(numbers, target_sum, max_diff):
    pairs = find_pairs(numbers, target_sum, max_diff)
    if len(pairs) == 0:                                #если количество найденных пар равно 0, то функция возвращает пустой список.
        return []
    elif len(pairs) == 1:                              #если количество найденных пар равно 1, то функция возвращает эту пару.
        return pairs
    else:                                              #иначе функция разбивает список на две части и рекурсивно вызывает саму себя для каждой из этих частей.
        mid = len(numbers) // 2
        left_pairs = minimize_pairs(numbers[:mid], target_sum, max_diff) 
        right_pairs = minimize_pairs(numbers[mid:], target_sum, max_diff)
        if len(left_pairs) == 0:                       #cравнивнение результатов, полученных для левой и правой частей.
            return right_pairs
        elif len(right_pairs) == 0:
            return left_pairs
        else:
            return left_pairs if len(left_pairs) < len(right_pairs) else right_pairs

numbers = fractions
target_sum = 6
max_diff = 2
pairs = minimize_pairs(numbers, target_sum, max_diff)
print(pairs)
