# 6. Вводится дата в формате dd.mm.yyyy. Вывести дату в формате mm\dd\yyyy.

# Ввод даты
my_date = input("Введите дату в формате dd.mm.yyyy: ")

# Замена "." на "\"
my_date_new = my_date.replace(".", "\\")

# Вывод даты в формате mm\dd\yyyy
print(f"Дата в формате mm\dd\yyyy: {my_date_new[3:6] + my_date_new[0:3] + my_date_new[6:]}.")