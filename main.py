file="passwds.md"
import random
import time
import string

print("[n]ew password, [l]ist all passwords, [c]hange an existing password\n")
print("your choice:")
if input("") == "n":
    pwd_length = int(input("password length:"))
    p = []
    for x in range(0,l):
        p.insert(pwd_length, random.choice(string.ascii_letters + string.digits + string.punctuation))
        print(p, "\n")
        print("Do you want to save the password to a file? (Y/N, [custom/file/path])")
        if input("Your Choice:") == "Y" or "y":
            print("")####
            

        
