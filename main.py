import csv
import os
import time


def esc(code):
    return f'\u001b[{code};1m'


def flag():
    for i in range(2):
        print(RED + '   ' * (3 - i) + WHITE + '   ' * i + RED + '   ' * 2 + END)
    print(RED + '   ' + WHITE + '   ' * 3 + RED + '   ' + END)
    for i in range(2):
        print(RED + '   ' * (i + 2) + WHITE + '   ' * (3 - i - 2) + RED + '   ' * 2 + END)
    return ''


def uzor(count_str, count_stolb):
    for j in range(count_stolb):
        for i in range(3):
            v = PINK + '   ' * (2 - i) + BLUE + '   ' + PINK + '   ' * (i * 2) + BLUE + '   ' + PINK + '   ' * (
                    2 - i) + END
            print((v + v) * count_str)
        for i in range(3):
            n = PINK + '   ' * i + BLUE + '   ' + PINK + '   ' * (4 - i * 2) + BLUE + '   ' + PINK + '   ' * i + END
            print((n + n) * count_str)
    return ''


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j]) + ' '
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + ' ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


RED = esc(41)
WHITE = esc(47)
END = esc(0)
BLACK = esc(48)
GREEN = esc(42)
PINK = esc(45)
BLUE = esc(46)

# сгенерировать изображение флага Швейцарии

print("Флаг Швейцарии: ")
print(flag())

# сгенерировать повторяющийся узор

print("Повторяющийся узор: ")
print(uzor(3, 1))  # в аргументах нужно указать, сколько раз повторить узор вправо и вниз

# задание c  файликом из прошлой лабораторной

books_16 = 0
with open('books.csv', 'r') as csvfile:
    table = list(csv.reader(csvfile, delimiter=';'))
    title = table.pop(0)
    all_books = len(table)
    for row in table:
        if int(row[5]) == 16:
            books_16 += 1
    percent_16 = books_16 * 100 // all_books
print("Диаграмма " + '\n')
print(GREEN + " " * percent_16 + END + '  16 y.o. ' + '\n')
print(GREEN + " " * (100 - percent_16) + END + '  others ' + '\n')

# построить график функции y = x/3

print('График функции y = x/3')

array_plot = [[0 for col in range(10)] for row in range(10)]  # создали массив аргументов

result = [0 for i in range(10)]  # создали массив со значением функции

for i in range(10):  # заполнили массив значений
    result[i] = i * 1 / 3

step = round(abs((result[9] - result[0])) / 9, 1)  # вычислили шаг аргумента и округлили до одного знака

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

# конец основной части лабораторной работы, начало доп задания

time.sleep(2)
os.system("cls")

# pic 1
print(WHITE + ' ' * 4 + GREEN + ' ' + WHITE + ' ' * 3 + END)
print(WHITE + ' ' * 3 + GREEN + ' ' * 2 + WHITE + ' ' + GREEN + ' ' + WHITE + ' ' + END)
print(WHITE + ' ' * 4 + GREEN + '  ' + WHITE + ' ' * 2 + END)
for i in range(2):
    print(WHITE + ' ' * 4 + GREEN + ' ' + WHITE + ' ' * 3 + END)
time.sleep(2)
os.system("cls")

# pic 2
print(WHITE + ' ' * 3 + RED + '   ' + WHITE + ' ' * 2 + END)
print(WHITE + ' ' * 4 + GREEN + ' ' + WHITE + ' ' * 3 + END)
print(WHITE + ' ' * 3 + GREEN + ' ' * 2 + WHITE + ' ' + GREEN + ' ' + WHITE + ' ' + END)
print(WHITE + ' ' * 4 + GREEN + '  ' + WHITE + ' ' * 2 + END)
for i in range(2):
    print(WHITE + ' ' * 4 + GREEN + ' ' + WHITE + ' ' * 3 + END)
time.sleep(2)
os.system("cls")

# pic 3
print(WHITE + ' ' * 2 + RED + ' ' + WHITE + ' ' + RED + ' ' + WHITE + ' ' + RED + ' ' + WHITE + ' ' + END)
print(WHITE + ' ' * 3 + RED + ' ' + WHITE + ' ' + RED + ' ' + WHITE + ' ' * 2 + END)
print(WHITE + ' ' * 4 + RED + ' ' + WHITE + ' ' * 3 + END)
print(WHITE + ' ' * 4 + GREEN + ' ' + WHITE + ' ' * 3 + END)
print(WHITE + ' ' * 3 + GREEN + ' ' * 2 + WHITE + ' ' + GREEN + ' ' + WHITE + ' ' + END)
print(WHITE + ' ' * 4 + GREEN + '  ' + WHITE + ' ' * 2 + END)
for i in range(2):
    print(WHITE + ' ' * 4 + GREEN + ' ' + WHITE + ' ' * 3 + END)

time.sleep(5)
