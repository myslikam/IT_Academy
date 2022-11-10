# Написать программу которая находит ближайшую степень двойки к введенному числу.
# 10(8), 20(16), 1(1), 13(16)

# новое решение с бинарными операторами
def degree_n():
    n = int(input("Введите число: "))
    a_low = 0
    a_up = 0
    for i in range(n, 0, -1):
        if ((i & (i - 1)) == 0):
            a_low = i
            break
    m = 2**n
    for i in range(n, m):
        if ((i & (i - 1)) == 0):
            a_up = i
            break
    if n - a_low < a_up - n:
        print(a_low)
    else:
        print(a_up)

degree_n()


# Старое решение

# def degree_n():
#
#     a = int(input("Введите число: "))
#     a_low = 2 ** (a.bit_length()-1)
#     a_up = 2 ** (a.bit_length())
#     if a - a_low < a_up - a:
#         print(a_low)
#     else:
#         print(a_up)
#
# degree_n()