# 6.	Вводится число найти его максимальный делитель, являющийся степенью двойки.
# 10(2) 16(16), 12(4).


numb = int(input("Введите число: "))

max_div = 1

for i in range(numb, 1, -1):
    if numb % i == 0 and i == (2 ** (i.bit_length()-1)):
        if max_div < i:
            max_div = i
            print(max_div)


