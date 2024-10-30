from sp_game import start_1p_game
import random
from question_loader import load_questions, save_results, ask_question, get_answer_to_question, check_the_answer

file_name = 'Q&A.csv'
output_file_name = 'Q&A_points.txt'


def get_p_number():
    input_str = input("How many players?\n")
    if input_str.isdigit():
        player_number = int(input_str)
        if player_number == 1:
            print("Opening single player mode")
            start_1p_game()
            exit()
        elif player_number in range(1, 6):
            print(f"Opening the game for {player_number} players")
            return player_number
        elif player_number >= 6:
            print("Too many players. Game only available up to 5 players. Choose again")
            return get_p_number()
        else:
            print("Incorrect input, choose a number between 1 and 5")
            return get_p_number()
    else:
        print("Incorrect input, choose a number between 1 and 5")
        return get_p_number()


def create_player():
    player_name = input("What's your name?\n")
    return player_name


def start_mp_game():
    num_players = get_p_number()
    player_dict = {}
    for i in range(num_players):
        print(f"Player {i + 1}")
        player_dict[create_player()] = 0
    mp_quiz_game(player_dict)


def mp_quiz_game(player_info):
    questions = load_questions(file_name)
    random.shuffle(questions)
    for i in questions:
        for j in player_info.keys():
            print(f"{j}'s turn:")
            ask_question(i)
            player_answer = get_answer_to_question()
            if check_the_answer(player_answer, i) == 1:
                player_info[j] += 1
    for k in player_info.keys():
        user_profile = str(f"{k} scored {player_info[k]} points")
        save_results(output_file_name, user_profile)
        print(user_profile)
