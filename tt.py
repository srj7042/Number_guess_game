import random
num = random.randint(1, 100)
takes = 0
print(" Guess the numbers between 1 and 100")
while True:
    guess = int(input("what is ur guess: "))
    takes += 1
    if guess < num:
        print("Too low! Nahh")
    elif guess > num:
        print("Too high! ")
    else:
        print(f"Correct! You guessed it in {takes} tries.")
        break
