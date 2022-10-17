# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.

n_country = int(input("Веведите количсетво стран: "))
my_dict = {}

for i in range(n_country):
    # Ввод списков, разбиваем их на слова
    str_input = input(f"Веведите список {i+1}-ю страну и ее города: ").split()

    # передаим информацию в словарь my_dict из введенных списков: ключ - город, значение страна
    for i in range(1, len(str_input)):
        my_dict[str_input[i]] = str_input[0]

n_city = int(input("Веведите количество городов: "))

# Цикл для вывода значений по ключу
for i in range(n_city):
    city_input = str(input(f"Веведите {i + 1} город: "))
    print(my_dict[city_input])

