###################### Решение 1
# import random
# from random import randint
#
#
# def rand_int_generator(min, max):
#     ammout = max - min
#     res = {}
#     for i in range(ammout):
#         x = random.randint(min, max)
#         res[f"elem no {i}"] = x
#     return res
#
#
# print(rand_int_generator(10, 15))
######################## Решение 2
from time import time


def time_random():
    return time() - float(str(time()).split('.')[0])


def rand_int_generator(min, max):
    ammout = max - min
    res = {}
    for i in range(ammout):
        rand_int = int(time_random() * (max - min) + min)
        res[f"elem no {i}"] = rand_int
    return res


print(rand_int_generator(1, 5))
