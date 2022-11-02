# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел, отсортированных
# по возрастанию, которая этот список “сворачивает”

from itertools import groupby
from operator import itemgetter

def get_ranges(data):
    data_2 = []
    for k, g in groupby(enumerate(data), lambda m: m[0] -m[1]):
        data_2.append(list(map(itemgetter(1), g)))

    def get_ran(a):
        n = ''
        for i in a:
            if len(i) == 1:
                n = n + str(min(i)) + ','
            else:
                n = n + str(min(i)) + '-' + str(max(i))+','
        print('"' + n[:len(n)-1] + '"')

    get_ran(data_2)

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4,7,10])
get_ranges([2, 3, 8, 9])

# ======Результат======
# "0-4,7-8,10"
# "4,7,10"
# "2-3,8-9"


