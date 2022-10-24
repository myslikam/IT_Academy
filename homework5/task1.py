# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner.
# a.	runner() – все фукнции вызываются по очереди
# b.	runner(‘func_name’) – вызывается только функцию func_name.
# c.	runner(‘func’, ‘func1’...) - вызывает все переданные функции

def  func1():
    print('==========Фукция 1==========')
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def func2():
    print('==========Фукция 2==========')
    my_lst = [1, 3, 'a', 1, 'b', 'b', 8, 135]
    lst_new = []
    for i in my_lst:
        if my_lst.count(i) == 1:
            lst_new.append(i)
    print(lst_new)

def  func3():
    print('==========Фукция 3==========')
    num_lst = [15, 0, 22, 3, 0, 256, 0, 111]
    for i in range(0, len(num_lst)):
        if num_lst[i] == 0:
            del num_lst[i]
            num_lst.append(0)
    print(num_lst)

def func4():
    print('==========Фукция 4==========')
    my_dict = {i: i ** 3 for i in range(1, 21)}
    print(my_dict)

# ================== РЕШЕНИЕ ===================

def runner(*args):
    if len(args) == 0:
        func1()
        func2()
        func3()
        func4()
    else:
        for i in args:
            globals()[i]()

runner()
runner('func3')
runner('func2', 'func4')