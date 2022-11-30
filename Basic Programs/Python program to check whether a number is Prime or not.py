# Given a positive integer N, The task is to write a Python program to check if the number is Prime or not in Python.

# Examples: 

# Input:  n = 11
# Output: True


# Input:  n = 1
# Output: False


def is_prime(x):
    if x > 1:
        for i in range(2, int((x/2)+1)):
            if (x % i) == 0:
                print("Given number is not prime")
                break
        else:
            print("This number is prime")
    else:
        print("Not prime")


number = int(input("Enter your number: "))
print(is_prime(number))