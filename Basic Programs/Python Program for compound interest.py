# Let us discuss the formula for compound interest. The formula to calculate compound interest annually is given by: 

# A = P(1 + R/100) t 

# Compound Interest = A – P 

# Where, 
# A is amount 
# P is the principal amount 
# R is the rate and 
# T is the time span

def compound_interest(P, R, T):
    A = P * (1 + (R / 100)) ** T
    Result = A - P
    return A 

print(compound_interest(1200, 5.4, 2)) 