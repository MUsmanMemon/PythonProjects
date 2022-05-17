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

def computer_guess(x):
    low = 1;
    high = x;
    feedback = "";
    while feedback != "c":
        if low != high:
            guess = r.randint(low,high)
        else:
            guess = low;
        feedback = input(f"Is {guess} too high (H), too low(L), or correct(C)?").lower();
        if feedback=='h':
            high = guess-1;
        elif feedback=='l':
            low = guess+1;

    print(f"Yayyy!!! the robot has guessed your the number {guess}, correctly.")

computer_guess(10)