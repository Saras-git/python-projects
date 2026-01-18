import random
print("Hi! Welcome to the number Guessing Game\n You have a 7 chances to guess the number. Let's Start")
low=int(input("enter the lower number : "))
high=int(input("enter the higher number : "))
print(f"\n You have a 7 chances to guess the number between {low} and {high}. Let's Start!")
number=random.randint(low,high)
chances=7
guess_number=0
while guess_number < chances:
    guess_number+=1
    guess=int(input("enter your guess : "))
    if guess == number:
        print(f"Correct! The number is {number}. You guessed it in {guess_number} attempts.")
        break
    elif guess_number >= chances and guess!=number:
        print(f"Sorry! The number was {number}. Better luck next time.")
    elif guess > number:
        print("too high! try a lower number")
    elif guess < number:
        print("Too low! try a higher number")