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
---'    ____)____
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

mychoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

choices = [rock, paper, scissors]

print("You chose:")
print(choices[mychoice])

comchoice = random.randint(0, 2)
print("Computer chose:")
print(choices[comchoice])

if mychoice == comchoice:
    print("It's a tie!")
elif (mychoice == 0 and comchoice == 2) or \
     (mychoice == 1 and comchoice == 0) or \
     (mychoice == 2 and comchoice == 1):
    print("You won!")
else:
    print("You lost!")
