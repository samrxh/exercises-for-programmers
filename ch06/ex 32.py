from random import randint


def number_finder(level):
    correct_number = None
    if level == '1':
        correct_number = randint(1, 10)
        print(correct_number)
    elif level == '2':
        correct_number = randint(1, 100)
        print(correct_number)
    elif level == '3':
        correct_number = randint(1, 1000)
        print(correct_number)
    else:
        print('Pick 1, 2, or 3.')
    return correct_number


def user_guesses():
    play_again = None
    while play_again != 'n':
        user_level = input("Pick a difficulty level (1, 2, or 3): ")
        num = number_finder(user_level)
        guess_amount = 1
        guess_list = {None}
        while play_again != 'n':
            try:
                guess = int(input("Guess: "))
                if guess in guess_list:
                    print("You already guessed that number. Guess again.")
                    guess_amount += 1
                    continue
                guess_list.add(guess)
                if guess < num:
                    print("Too low. Guess again. ")
                    guess_amount += 1
                elif guess > num:
                    print("Too high. Guess again. ")
                    guess_amount += 1
                elif guess == num:
                    print(f"You got it in {guess_amount} guesses.")
                    guess_list = {None}
                    if guess_amount == 1:
                        kudos = "You're a mind reader!"
                    elif guess_amount < 5:
                        kudos = "Most impressive."
                    elif guess_amount < 7:
                        kudos = "You can do better than that."
                    else:
                        kudos = "Better luck next time."
                    print(kudos)
                    break
            except ValueError:
                print("Please choose a number.")
                guess_amount += 1
        play_again = input("Play again? Enter 'n' to exit. ")
    print("Goodbye.")


print("Let's play guess the number.")
user_guesses()

# challenges:
# map guess_amount to some comments
# keep track of previous guesses, issue alert if user already guessed number, count as a wrong guess
