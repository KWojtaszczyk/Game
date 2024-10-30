from sp_game import start_1p_game
from mp_game import start_mp_game


def choice(number):
    if number == '1':
        return start_1p_game()
    elif number == '2':
        return start_mp_game()
    elif number == '3':
        exit()
    else:
        new_number = input("Incorrect input, choose an option:\n")
        return choice(new_number)


def show_menu():
    print("Welcome to the QuizGame!")
    print("A game to check your knowledge in many areas.\n")
    print("Choose:")
    print("1 - start a single-player game.")
    print("2 - start a multiplayer game.")
    print("3 - exit the game.")

