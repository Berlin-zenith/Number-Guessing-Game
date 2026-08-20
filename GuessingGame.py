# July 13th, 2026 | Day 31 [ Guessing Game ] First Project !
# 1. Code that makes the computer choose a random number ✔️
# 2. Get User's Input (always a number so int) ✔️
# 3. Return statements "too high" or "too low" BASED on User input + "close" to make it easier for User✔️
# 4. Def Function for opening display of the program + ending of the program ✔️

import random
secret_number = random.randint(1, 10) # <--- main part of the program
# Opening Function Display
def display(text): # will use this function twice
    print("♢♦︎" * 7, f"\n --{text}--")
    print("♢♦︎" * 7)
display("GUESSING GAME")
print("Instructions: Guess The Number Between 1 and 30. [Till You Get It Right]") # INTRO DONE
count = 1
user_input = int(input("\nEnter Number: "))  # Getting User Input
print(f"Tries: {count}")
while user_input != secret_number:
    difference = abs(user_input - secret_number)
    if difference <= 30:
        print("Getting Close...You Are Within 10 Numbers!")  # within range?
    elif user_input < secret_number:  # too low ?
        print("Too Low!")
    else:
        print("Too High!")  # too high? (last condition)
    count += 1
    user_input = int(input("\nEnter Number: "))
    print(f"Tries: {count}")
print("\n :0 ... !!")
display("CORRECT! GAME OVER")