from sp_game import start_1p_game
from mp_game import start_2p_game
from results import show_scores


def choice(number):
    if number == '1':
        start_1p_game()
    elif number == '2':
        start_2p_game()
    elif number == '3':
        show_scores()
    elif number == '4':
        exit()
    else:
        new_number = input("Incorrect input, choose an option:")
        choice(new_number)


def show_menu():
    print("Welcome to the QuizGame!")
    print("A game to check your knowledge in many areas.\n")
    print("Choose:")
    print("1 - start a single-player game.")
    print("2 - start a multiplayer game.")
    print("3 - show previous scores.")
    print("4 - exit the game.")

