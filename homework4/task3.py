# 3.	Даны два списка чисел. Посчитайте, сколько различных чисел
# содержится одновременно как в первом списке, так и во втором.

list_num_1 = [2, 8, 12, 16, 12]
list_num_2 = [2, 668, 8, 46542, 545, 16]

# Преобразуем списки в множества и их объединим, при этом останутся только различные числа
num_set = set(list_num_1) | set(list_num_2)
print(f"Количество различных чисел равно: {len(num_set)}")