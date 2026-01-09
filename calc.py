a=7
b=5
c=a+b
print("the sum of a and b is " + str(c))
d=a-b
print("the substraction of a amd b is " + str(d))
e=a*b
print("the multiplication of a and b is " + str(e))
f=a/b
print("the division of a and b is " + str(f))
print(a//b)
print(a**b)


num1= int(input("enter first number "))

if num1 > 0:
    print("the number is positive")
elif num1 < 0:
    print("the number is negative")
else:
    print("the number is zero")