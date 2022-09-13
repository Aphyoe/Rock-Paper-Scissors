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


player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0, 2)

if player_choice == 0 and computer_choice == 0:
    print(f"{rock}\n Computer chose:\n {rock}\n It's a draw")
elif player_choice == 0 and computer_choice == 1:
    print(f"{rock}\n Computer chose:\n {paper}\n You lose")
elif player_choice == 0 and computer_choice == 2:
    print(f"{rock}\n Computer chose:\n {scissors}\n You win")
elif player_choice == 1 and computer_choice == 0:
    print(f"{paper}\n Computer chose:\n {rock}\n You win")
elif player_choice == 1 and computer_choice == 1:
    print(f"{paper}\n Computer chose:\n {paper}\n It's a draw")
elif player_choice == 1 and computer_choice == 2:
    print(f"{paper}\n Computer chose:\n {scissors}\n You lose")
elif player_choice == 2 and computer_choice == 0:
    print(f"{scissors}\n Computer chose:\n {rock}\n You lose")
elif player_choice == 2 and computer_choice == 1:
    print(f"{scissors}\n Computer chose:\n {paper}\n You win")
elif player_choice == 2 and computer_choice == 2:
    print(f"{scissors}\n Computer chose:\n {scissors}\n It's a draw")
else:
  print("You typed an invalid number, you lose by default.")
