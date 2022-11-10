# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)

def my_dec(func):

    def wrapper(*args):
        out = func(*args)
        my_txt = open("data_hw5/task2.txt", 'a')
        my_txt.write(str(out)+'\n')
        my_txt.close()
        return out

    return wrapper


@my_dec
def my_func(my_num):
    return my_num * 1000


my_func(50)
my_func(33)
my_func(1658)


