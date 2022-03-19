import random
from tkinter import END
print("Number Guessing Game")
num = random.randint(1,9)
chances = 5
print("Guess a number between 1 and 9")

while chances > 0:

    guess = int(input("What is your guess? "))

    if guess == num:
        print("Congratulations, YOU WIN!!") 
    
    elif guess < num:
     print("Your guess was too low, guess a number higher than", guess)

    else:
        print("Your guess was too high, guess a number lower than", guess)

    chances -= 1

if not chances < 0:
    print("You lose! the correct answer is", num)