# Вариант 1
# Создание цикла от 1 до 100 (функцией range)
for i in range(1, 101):
    # Проверка одновременной кратности чиселам 3 и 5
    if i % 3 == 0 and i % 5 == 0:
    # Проверку можно можно выполнить i % 15 ==0, так код будет более короче
    # if i % 15 == 0:
        print("FizzBuzz")
    # Проверка  кратности числу 3
    elif i % 3 == 0:
        print("Fizz")
    # Проверка  кратности числу 5
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# # Вариант 2 с созданием списка, и записью в него полученного результата
#
# # Создадим пустой список, в который будем записывать результат
# my_fizzbuzz = []
#
# for i in range(1, 101):
#     if i % 15 == 0:
#         my_fizzbuzz.append("FizzBuzz")
#     elif i % 3 == 0:
#         my_fizzbuzz.append("Fizz")
#     elif i % 5 == 0:
#         my_fizzbuzz.append("Buzz")
#     else:
#         my_fizzbuzz.append(i)
#
# print(my_fizzbuzz)