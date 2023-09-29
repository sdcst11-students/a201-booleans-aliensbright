#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
Num = float(input('Enter an number.'))
y = Num%1
if y==0:
    Num=int(Num)
    print(f'{Num} is an integer.')
if y!=0:
    print(f'{Num} is not an integer.')