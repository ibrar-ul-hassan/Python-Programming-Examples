# Python Program for factorial of a number

# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.

# Factorial Formula = n * (n-1) * (n-2) * ...... 1

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        Num = 1
        while (n > 1):
            Num *= n
            n -= 1
        return Num


print(factorial(3)) 
print(factorial(6)) 