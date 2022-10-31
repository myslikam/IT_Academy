# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел, отсортированных
# по возрастанию, которая этот список “сворачивает”


# Не готова











# nums =[0, 1, 2, 3, 4, 7, 8, 10]
# ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
# iranges = iter(nums[0:1] + ranges + nums[-1:])
# print (', '.join([str(n) + '-' + str(next(iranges)) for n in iranges]))


nums =[0, 1, 2, 3, 4, 7, 8, 10]
ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
iranges = iter(nums[0:1] + ranges + nums[-1:])
print (', '.join([str(n) + '-' + str(next(iranges)) for n in iranges]))




# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
# "0-4,7-8,10"
# get_ranges([4,7,10])
#  # "4,7,10"
# get_ranges([2, 3, 8, 9])
# # "2-3,8-9"



# не готово
# def get_ranges(*args):
#
#     n = ''
#     for i in args:
#         if len(i) == 1:
#             n = n + str(min(i)) + ','
#         else:
#             n = n + str(min(i)) + '-' + str(max(i))+','
#     print('"' + n[:len(n)-1] + '"')
#
#
# get_ranges([1, 2, 3, 4], [7, 8], [10])








# from itertools import groupby
# from operator import itemgetter
# data = [0, 1, 2, 3, 4, 7, 8, 10]
# for k, g in groupby(enumerate(data), lambda ix: ix[0] -ix[1] ):
#     print(list(map(itemgetter(1), g)))