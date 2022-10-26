# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

def my_dec(fun):
    n = 0
    def wrapper():
        nonlocal n
        n += fun()
        return n
    return wrapper

@my_dec
def my_func():
    return 5

print(my_func())
print(my_func())
print(my_func())


