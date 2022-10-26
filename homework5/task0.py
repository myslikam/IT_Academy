# Разное

import os
inpun_h = int(input("Введите номер homework: "))
inpun_n = int(input("Введите номер task: "))

def my_fun(h, n):
    os.system(f"e:/IT_Academy/Homework/homework{h}/task{n}.py")

my_fun(inpun_h, inpun_n)
