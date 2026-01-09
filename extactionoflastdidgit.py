num = int(input("Enter a number: "))
n = num

while n > 0:
    last_digit = n % 10
    print("The last digit of", n, "is", last_digit)
    n = n // 10

