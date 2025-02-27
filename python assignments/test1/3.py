import random
def get_input():
    guess = int(input("Guess a number between 1 and 100: "))
    return guess
def ngg():
    tn = random.randint(1, 100)
    while True:
        guess=get_input()
        if guess < tn:
            print("Too Low!")
        elif guess > tn:
            print("Too High!")
        else:
            print("Correct, You guessed the number!")
            break
def main():
    ngg()
    
main()
