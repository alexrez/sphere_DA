# Минимальная последовательность
# Постройте последовательность a1, a2, ... an из n положительных чисел от 1 до k, обладающую следующими свойствами: 
# 1. любые два соседних числа в последовательности различны: a1 ≠ a2, a2 ≠ a3, ... an-1 ≠ an; 
# 2. каждое число от 1 до k встречается в этой последовательности хотя бы один раз.
# Среди таких последовательностей требуется найти лексикографически минимальную.

# Формат входных данных: На вход вашей программе подается два целых числа n и k — длина и максимальное число (2 ≤ k ≤ n ≤ 10000).

# Формат результата: Выведите последовательность, удовлетворяющую описанным выше условиям, через пробел.

n, k = input().split(' ')
a_list = [i%2 or 2 for i in range(1, int(n) - int(k) + 3)]
b_list = [i for i in range(3, int(k) + 1)]

print(*(a_list+b_list))