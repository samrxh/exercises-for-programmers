from random import choice


def get_names():
    names = []
    while True:
        name = input("Enter a name: ")
        if name == '':
            break
        names.append(name)
    return names


def select_winner(names):
    winner = choice(names)
    names.remove(winner)
    return winner


def contestant_game():
    while True:
        another = None
        ls = get_names()
        while another != 'n':
            try:
                dub = select_winner(ls)
                print(f"The winner is {dub}.")
                another = input("Would you like to select another winner? Enter 'n' to exit. ")
            except IndexError:
                print("No more contestants in list.")
                break
        play_again = input("Would you like to play again? Enter 'n' to exit. ")
        if play_again == 'n':
            break


contestant_game()
