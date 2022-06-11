import os
import random
import string

file_name = input("enter file name : ")


def file_creating(file_name):
    dir = os.getcwd()
    print(dir)
    for file in os.listdir(dir):
        if file == file_name:
            open(f"{file}").close()
        else:
            open(f"{file_name}.txt", "a").close()

    char_number = int(input("enter number of characters : "))

    text_info = [random.choice(string.ascii_letters) for x in range(char_number)]
    numeric_info = [random.choice(string.digits) for x in range(char_number)]

    res = [x+y for x,y in zip(text_info, numeric_info)]

    with open(f"{file_name}.txt", "w") as f:
        for i in res:
            f.write(str(i))


file_creating(file_name)


def read_file():
    with open(f"{file_name}.txt", "r") as f:
        print(f.readlines())


read_file()