# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

def my_dec(fun):
    def wrapper(a):
        my_txt = open("data_hw5/task2.txt", 'a')
        a += 10
        my_txt.write(str(a)+'\n')
        my_txt.close()
        return a
    return wrapper

@my_dec
def my_func(my_num):
    return my_num

my_func(50)
my_func(33)
my_func(1658)



# Старое решение
# def my_dec(fun):
#     n = 0
#     def wrapper():
#         nonlocal n
#         n += fun()
#         return n
#     return wrapper
#
# @my_dec
# def my_func():
#     return 5
#
# print(my_func())
# print(my_func())
# print(my_func())


