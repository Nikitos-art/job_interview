from math import trunc, modf


def user_number():
    number = float(input("Enter your number : "))
    if number % 1 != 0:
        print(f"Number {number} is a float")
        total_num = (modf(number))
        num1 = total_num[1]
        num2str = str(total_num[0])
        num2 = int(num2str[2:])
        print(num1, num2)
        if num1 > num2:
            print(True)
        else:
            print(False)
    else:
        print(f"Number {number} is a whole number")


user_number()

# from math import trunc, modf
#
# def user_number():
#     number = float(input("Enter your number : "))
#     if number % 1 != 0:
#         print(f"Number {number} is a float")
#         print(trunc(number))
#         print(modf(number))
#     else:
#         print(f"Number {number} is a whole number")
#
# user_number()
