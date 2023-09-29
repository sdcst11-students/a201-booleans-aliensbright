#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"
Num = int(input('Enter an integer.'))
y = Num%2
if y==0:
    print(f'{Num} is even.')
if y!=0:
    print(f'{Num} is odd.')