# import os
#
# # очень долго сидел с этим заданием и ничего кроме костыля crutch не придумал. Цикл отсанавливается
# # когда в директоррии видна папка Windows.
#
# def print_directory_contents(path):
#     crutch = []
#     while "Windows" not in crutch:
#         dirs = os.listdir(path)
#         crutch = dirs
#         print(dirs)
#         path += "/.."
#
#
# p = "C:/Users/PC/PycharmProjects"
# print_directory_contents(p)

#####################################################
import os

# from pathlib import Path
#
#
# dir = "C:/Users/PC/PycharmProjects"
#
#
# def print_directory_contents(directory):
#     while directory != "C:/":
#         files = Path(directory).glob('*')
#         for file in files:
#             print(file)
#     directory =
#
# print_directory_contents(dir)
######################################################
import os
from pathlib import Path

direct = Path("C:/Users/PC/PycharmProjects")

def print_directory_contents(directory):
    for file in os.listdir(directory):
        print(file)
        x = os.path.join(directory, file)
        if os.path.isdir(x):
            print_directory_contents(x)


