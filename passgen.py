import random 
import string   
print('''SELECT THE DIFFICULT BY ITS LENGTH
  1:EASY-ENTER LENGTH BELOW 6
  2:MEDIUM-ENTER LENGTH IS B/W 6-10
  3:HARD:ENTER LENGTH ABOVE 10''')

l=int(input("ENTER THE LENGTH OF THE PASSWORD:"))
password=""
for i in range(l):
    ch=random.randint(1,3)
    if ch==1:
        char=random.choice(string.ascii_letters)
        password+=char
    elif ch==2:
        char=random.randint(0,9)
        password+=str(char)
    elif ch==3:
        char=random.choice(string.punctuation)
        password+=char
print(password)