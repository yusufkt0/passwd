file="~/passwd.md"
import random
import time
import string
l=int(input("passwd lenght:"))
chars=[]
for x in range(0,l):
    chars.insert(l,random.choice(string.ascii_letters + string.digits + string.punctuation))
for y in chars:
    print(y,end="")
    #write passwd to home dir
    #f=open(file,"a")
    #f.write(y)
time.sleep(5)
