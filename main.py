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

cpu_choice = random.randint(1, 3)

print(" Welcome to the most chanlenging rock paper scissor tournament.")
user_choice = int(input("Please enter 1 for rock, 2 for paper or 3 for scissors."))

#evaluate user choice

if user_choice == 1:
  print("USER CHOICE")
  print(rock)
elif user_choice == 2:
  print("USER CHOICE")
  print(paper)
elif user_choice == 3:
  print("USER CHOICE")
  print(scissors)
else:
  print("Please chooce a number between 1 to 3")

#evaluate cpu choice

if cpu_choice == 1:
  print("CPU CHOICE")
  print(rock)
elif cpu_choice == 2:
  print("CPU CHOICE")
  print(paper)
else:
  print("CPU CHOICE")
  print(scissors)

#evaluating who's winning

if user_choice == 1 and cpu_choice == 3:
  print("You win")

if user_choice == 3 and cpu_choice == 1:
  print("The computer win")

if user_choice == 3 and cpu_choice == 2:
  print("You win")

if user_choice == 2 and cpu_choice == 3:
  print("The computer win")

if user_choice == 1 and cpu_choice == 2:
  print("The computer win")

if user_choice == 2 and cpu_choice == 1:
  print("You win")

if user_choice == cpu_choice:
  print("It's a draw")