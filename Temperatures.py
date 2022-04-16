import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n = int(input())  # the number of temperatures to analyse
# print(f"{i}, {t}, {n}", file=sys.stderr, flush=True)
number_list=[-8, -2, 1, 4, 5]
# number_list = [-137, -12, -5]
# number_list = [-5, 5, 12, 21, 24, 42]
# number_list = [-40, -5, -4, -2, 2, 4, 5, 11, 12, 18]
# number_list = []
n=int(len(number_list))
negative_numbers = []
positive_numbers = []
for i in number_list:
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    print(f"{negative_numbers}", file=sys.stderr, flush=True)
    print(f"{positive_numbers}", file=sys.stderr, flush=True)
    print(f"{t}, {n}", file=sys.stderr, flush=True)
    # print (type(i), type(t), type(n), type(negative_numbers), type(positive_numbers))
    if t < 0:
        negative_numbers.append(t)
    elif t > 0:
        positive_numbers.append(t)
    negative_numbers.sort(reverse=True)
    positive_numbers.sort()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(f"{negative_numbers}", file=sys.stderr, flush=True)
print(f"{positive_numbers}", file=sys.stderr, flush=True)
negative_number = negative_numbers[0] * 2 - negative_numbers[0]
if negative_number > positive_numbers[0]:
    result = positive_numbers[0]
elif negative_number < positive_numbers[0]:
    result = negative_number
elif t == 0:
    result = 0
elif t == 1:
    result = 1
print(result)
