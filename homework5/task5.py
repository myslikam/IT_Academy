# Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

def degree_n():
    a = int(input("Введите число: "))
    if a < 3:
        print(1)
    elif a % 2 == 0 and (a & (a - 1) != 0):
        print(2 ** (a.bit_length()-1))
    elif a % 2 != 0 and (a & (a - 1) != 0):
        print(2 ** (a.bit_length()))
    else:
        print(a.bit_length()-1)

degree_n()
