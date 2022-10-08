# 1 Вывод информации

print('Hello, IT-Academy')


# 2 Запрос имени пользователя, вывод приветсвия по имени

name = input('Как ваз зовут?\n')
print('Привет, %s.' %name)


# 3 Перечиление списка имен, с выводом информации в виде пронумерованного списка

friends =['Саша', 'Даша', 'Люда', 'Юля']
for i, name in enumerate(friends):
    print("Номер {itration} это {name}".format(itration=i, name=name))


# 4 Цикл для определения последовательности числел Фибоначчи до 100

parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


# 5 Функция вывода приветствия по заданому имени

def greet(name):
    print("Привет", name)

greet('Саша')
greet('Даша')
greet('Люда')


# 6 Проверка номера телефона на соотвествие формату г. Гомель

import re
for test_string in ['75-25-12', 'ILL-EGAL', '645-53-356']:
    if re.match(r'^\d{2}-\d{2}-\d{2}$', test_string):
        print(test_string, 'этот номер является местным номером г. Гомель')
    else:
        print(test_string, 'этот номер отклонен')


# 7 Расчет сумарной стоимости продуктов

prices = {'apple': 0.4, 'banana': 0.5}
my_purchase = {'apple': 1, 'banana': 6}
grocery_bil = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
print('I owe the grocer $%.2f % grocery_bil')


# 8 Расчет суммы целых чисел

import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum=', total)
except ValueError:
    print('Please supply integer arguments')


# 9 Вставка имени файла

import glob
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print('   ------' + file_name)

    with open(file_name) as f:
        for line in f:
            print('   ' + line.rstrip())

    print()


# 10 Проверка текущего времени на соотвествие графику активности, отдыха и т.д.

from time import localtime
activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting'}

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print('Unknown, AFK or sleeping!')


# 11 Автоматическая считалочка

piglet = '''
%d поросят пошли купаться к морю,
%d поросят резвились на просторе,
Один из них утоп – ему купили гроб,
И вот вам результат: стало %d поросят!
'''
pig = 10
while pig > 1:
    print(piglet %(pig, pig, pig - 1))
    pig -=1


# 12 Расчет отстатка средств на текущем счете

class BankAccount(object):
    def __init__(self, inital_balance=0):
        self.balance = inital_balance
    def deposit(self, amount):
        self.balance +=  amount
    def withdraw(self, amount):
        self.balance -= amount
    def owerdrawn(self):
        return self.balance < 0
my_account = BankAccount(1000000)
my_account.withdraw(50)
print(my_account.balance, my_account.owerdrawn())


# 13 Тест средней скорости

import unittest
def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size-1)/2)]
    else:
        return (copy[int(size/2-1)] + copy[int(size/2)])/2
class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
if __name__ == '__main__':
    unittest.main()


# 14 Автоматическое тестирование

def median(pool):
    '''Statistical median to demonstrate doctest.
    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    6 #change to 7 in order to pass the test
    '''
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size/2 - 1)] + copy[int(size/2)]) / 2
if __name__ == '__main__':
    import doctest
    doctest.testmod()


# 15 Вывод параграфов

from itertools import groupby
lines = '''
This is the first paragraph.

This is the second.
'''.splitlines()
# Use itertools.groupby and boll return groups of
# consecutive lines that either have content or don't
for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print (' '.join(frags))
# Prints:
# This is the first paragraph.
# This is the second.


# 16 Запись информации в файл, и чтение

import csv

# need to define cmp function in Python 3
def cmp(a,b):
    return (a > b) - (a < b)

# write stocks data as comma-separated values
with open('stocks.csv', 'w', newline='') as stocksFileW:
    writer = csv.writer(stocksFileW)
    writer.writerows([
        ['GOOG', 'Google, Inc.', 505.24, 0.47, 0.09],
        ['YHOO', 'Yahoo! Inc.', 27.38, 0.33, 1.22],
        ['CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.4901]
    ])

# read stoks, print status messages
with open('stocks.csv','r') as stocksFile:
    stocks = csv.reader(stocksFile)

    status_labels = {-1: 'doen', 0: 'unchanged', 1: 'up'}
    for ticker, name, price, change, pct in stocks:
        status = status_labels[cmp(float(change), 0.0)]
        print('%s is %s (%.2f)' % (name, status, float(pct)))


# 18 Определение ходов Королевы в шахматах

BOARD_SIZE = 8

def under_attack(col, queens):
    left = right = col

    for r, c in reversed(queens):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
        return False

def solve(n):
    if n == 0:
        return[[]]
    smaller_solutions = solve(n - 1)

    return [solution+[(n,i+1)]
        for i in range(BOARD_SIZE)
            for solution in smaller_solutions
                if not under_attack(i+1, solution)]

for answer in solve(BOARD_SIZE):
    print(answer)


# 20 Генератор случайных чисел

import itertools
def inter_primes():
    # iterator of all numbers between 2 and infinity
    numbers = itertools.count(2)

    # generate primes forever
    while True:
        # get the first number from the iterantor (always a prime)
        prime = next(numbers)
        yield prime

        # This code iteratively builds up a chain of
        # Filters... slightly tricky, but ponder it a bit
        numbers = filter(prime.__rmod__, numbers)
for p in inter_primes():
    if p > 1000:
        break
    print(p)


# 21 Сбор данных с XML/HTML (парсинг)

dinner_recipe = '''<html><body><table>
<tr><th>amt</th><th>unit</th><th>item</th></tr>
<tr><td>24</td><td>slices</td><td>baguette</td></tr>
<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>
<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>
<tr><td>1</td><td>jar</td><td>pesto</td></tr>
</table></body></html>
'''


# From http://effbot.org/zone/element-index.htm

import xml.etree.ElementTree as etree
tree = etree.fromstring(dinner_recipe)

# For invalid HTML use http://effbot.org/zone/element-soup.htm
# import ElementSoup, StringIO
# tree = ElementSoup.parse(StringIO.StringIO(dinner_recipe))

pantry = set(['olive oil', 'pesto'])
for ingredient in tree.getiterator('tr'):
    amt, unit, item = ingredient
    if item.tag == "td" and item.text not in pantry:
        print ("%s: %s %s" % (item.text, amt.text, unit.text))


# 28 Определение ходов Королевы в шахматах

BOARD_SIZE = 8
class BailOut(Exception):
    pass

def validate(queens):
    left = right = col = queens[-1]
    for r in reversed(queens[:-1]):
        left, right = left-1, right+1
        if r in (left, col, right):
            raise BailOut

def add_queen(queens):
    for i in range(BOARD_SIZE):
        test_queens = queens + [i]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            else:
                return add_queen(test_queens)
        except BailOut:
            pass
    raise BailOut
queens = add_queen([])
print (queens)
print ("\n".join(". "*q + "Q " + ". "*(BOARD_SIZE-q-1) for q in queens))


# 33 Игра Угадай число от 1 до 20, с  шести попыток

import random

guesses_made = 0
name = input('Привет! Как тебя зовут?\n')
number = random.randint(1, 20)
print('Внимание вопрос, {0}, Угадай число от 1 до 20.'.format(name))

while guesses_made < 6:

    guess = int(input('Ваше число: '))
    guesses_made += 1

    if guess < number:
        print('Ваше число меньше загаданного')

    if guess > number:
        print('Ваше число больше загаданного')

    if guess == number:
        break

if guess == number:
    print('Ура, {0}! Вы отгадали номер с {1} попытки!'.format(name, guesses_made))
else:
    print('Не отгадал. Задуманное число равно - {0}'.format(number))
