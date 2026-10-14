import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
num = random.randint(1,100)

print("Select your difficulty:")
print("1. Easy (10 guesses)")
print("2. Medium (5 guesses)")
print("3. Hard (3 guesses)")

difficulty = int(input())
if difficulty == 1:
    allowed = 10
elif difficulty == 2:
    allowed = 5
else:
    allowed = 3

guess = int(input("Enter your guess: "))
guesses = 1
while guess != num and guesses < allowed:
    if num < guess:
        print(f"Incorrect! The number is less than {guess}")
    else:
        print(f"Incorrect! The number is greater than {guess}")
    guess = int(input("Enter your guess: "))
    guesses += 1

if guess == num:
    print(f"Congratulations! You guess the correct number in {guesses} attempts")
else:
    print(f"Defeat. You did not guess the number withing {allowed} attempts")