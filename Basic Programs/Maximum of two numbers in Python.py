# Given two numbers, write a Python code to find the Maximum of these two numbers.


def max(x,y):
    if x > y:
        return x
    else: 
        return y

first_number = 2
second_number = 5
print(max(first_number,second_number))