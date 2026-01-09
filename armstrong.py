n=int(input("Enter a number: "))
s=0
temp=n
while temp>0:
    digit=temp%10
    s+=digit**3
    temp//=10
if n==s:
    print(str(n) + " is an Armstrong number")
else:
    print(str(n) + " is not an Armstrong number")