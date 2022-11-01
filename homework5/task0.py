# Разное

# import os
# inpun_h = int(input("Введите номер homework: "))
# inpun_n = int(input("Введите номер task: "))
#
# def my_fun(h, n):
#     os.system(f"e:/IT_Academy/Homework/homework{h}/task{n}.py")
#
# my_fun(inpun_h, inpun_n)


list_numbers = [78, 99, 66, 44, 50, 30, 45, 15, 25, 20]
count = 0
count = sum(map(lambda i: i % 5 == 0, list_numbers))
print(    "количество элементов списка, удовлетворяющих заданному условию:",    count)