import os
from termcolor import colored

# path = "C:/Users/PC/OneDrive/Desktop/"


path = os.path.join('C:/Users/PC/OneDrive/Desktop/')
file_name = 'questions.txt'


def find_file(path, file_name):
    for file in os.listdir(path):
        if file == file_name:
            print(colored(os.path.splitext(file)[0],'red'), colored(os.path.splitext(file)[1], 'green'))


find_file(path, file_name)