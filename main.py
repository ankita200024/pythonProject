#task-4
#rock-paper-scissors game
'''import random
options = ('rock','paper','scissors')
playing=True
while playing:
    computer = random.choice(options)
    user=input("enter your choice (rock,paper,scissors):")
    print(f"user : {user}")
    print(f"computer : {computer}")
    if computer==user:
      print("its a tie!")
    elif user=="paper" and computer=="rock":
      print("you win!")
    elif user=="scissor" and computer=="paper":
      print("you win!")
    elif user=="rock" and computer=="scissor":
      print("you win!")
      break
    else:
      print("you loss!")

    play_again=input("play again?(yes/no):")
    if play_again=="no":
       playing=False
print("thanks for playing")'''



#task-3
#password generator
'''import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

while True:
    password_length = int(input("\nEnter the length of the password (at least 8 characters): "))
    if password_length >= 8:
        break
    else:
        print("\nPlease try again!")

password = generate_password(password_length)
print("\nYour generated password:", password)'''




#task 2
#simple calculator
'''a='+'
b='-'
c='*'
d='//'
while True:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    op=input( "enter '+' or '-' or '*' or '//' or'%' or '/':")
    if (op =='+'):
      z=x+y
      print(z)
    elif (op=='-'):
      z=x-y
      print(z)
    elif (op=='*'):
      z=x*y
      print(z)
    elif( op == '//'):
      z = x//y
      print(z)
    elif (op == '%'):
      z = x%y
      print(z)
    elif (op == '/'):
      z = x / y
      print(z)
    else:
      print("bye")
      break'''







