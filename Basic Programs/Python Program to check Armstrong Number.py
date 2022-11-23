# # Given a number x, determine whether the given number is Armstrong number or not.

# #  Examples

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

# Input : 120
# Output : No
# 120 is not a Armstrong number.
# 1*1*1 + 2*2*2 + 0*0*0 = 9



n = 153  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")