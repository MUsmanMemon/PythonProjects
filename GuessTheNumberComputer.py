import random as r

def guess(x):
    random_number = r.randint(1,x)
    guess = 0
    print(random_number)
    while(guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        # print(guess)
        if guess < random_number:
            print("Sorry guess again too low.")

        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yayy!, congratulation. You have guessed the number ({random_number}) correctly.")

guess(10)