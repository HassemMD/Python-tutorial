import random
import time
print("Welcome to the Guessing Game!")
time.sleep(2)
print("Let me pick a number from 1 to 10")
time.sleep(2)
number = random.randint(1,10)
guess = int(input("Choose a number : "))
guess_count = 1
while guess != number:
    guess_count += 1
    if guess > number:
       guess = int(input("a little LOWER! try again: "))
    else:
        guess = int(input("a little HIGHER! try again: "))
    if guess_count ==1:
        print(f"congratulations! you guessed the Correct number {number} in {guess_count} try!")
    else:
        print(f"congratulations! you guessed the Correct number {number} in {guess_count} tries!")
print("THANKS FOR PLAYING !!!"



