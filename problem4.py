#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""
a=float(input('Enter one side:'))
b=float(input('Enter a second side:'))
c=float(input('Enter third side:'))
if a>=b:
    if a>=c:
        largest=a
        small1=b
        small2=c
    else:
        largest=c
        small1=a
        small2=b
elif b>=c:
    largest=b
    small1=a
    small2=c
else:
    largest=c
    small1=a
    small2=b
hyp=(small1**2+small2**2)**0.5
percdiff=(hyp-largest)*2/(hyp+largest)*100
if 2>=percdiff>=-2:
    print('That is a right triangle.')
elif percdiff>2:
    print('That is an acute triangle.')
elif percdiff<-2:
    print('That is an obtuse triangle.')
