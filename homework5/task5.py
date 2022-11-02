# Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

def degree_n():
    a = int(input("Введите число: "))
    a_low = 2 ** (a.bit_length()-1)
    a_up = 2 ** (a.bit_length())
    if a - a_low < a_up - a:
        print(a_low)
    else:
        print(a_up)

degree_n()


