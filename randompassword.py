import random
import string

n = int(input("Enter the length of the password: "))
c = string.digits + string.ascii_letters + string.punctuation
password = " ".join(random.choice(c) for i in range(n))
print("password:", password)
                    
   