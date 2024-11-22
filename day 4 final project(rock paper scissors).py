import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("WELCOME TO ROCK PAPER AND SCISSORS\n\n")
a = int(input("What do you choose ? Type 0 for Rock , 1 for paper or 2 for scissors :\n"))
if a == 0:
    print(f"Your choice is \n {rock}")
if a == 1:
    print(f"Your choice is \n {paper}")
if a == 2:
    print(f"Your choice is \n {scissors}")

b = random.randint(0,2)

if b == 0:
    print(f"\n Computer\'s choice is \n {rock}")
if b == 1:
    print(f"\n computer\'s choice is \n {paper}")
if b == 2:
    print(f"\n computer\'s choice is \n {scissors}")


if a==0:
    if b == 0:
        print("\n Its a draw")
    elif b ==1:
        print("\nYou lose")
    else:
        print("\n you WIN!")


if a==1:
    if b == 1:
        print("\n Its a draw")
    elif b ==2:
        print("\nYou lose")
    else:
        print("\n you WIN!")

if a==2:
    if b == 2:
        print("\n Its a draw")
    elif b ==0:
        print("\nYou lose")
    else:
        print("\n you WIN!")