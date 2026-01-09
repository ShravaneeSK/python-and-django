n = int(input("Enter a number: "))
num = n
count = 0
while n > 0:
    count += 1
    n = n // 10
   
print("The number of digits in", num, "is", count)
