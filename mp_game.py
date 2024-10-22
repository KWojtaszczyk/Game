from sp_game import start_1p_game
import random
from question_loader import load_questions, save_results, ask_question, get_answer_to_question, check_the_answer, show_results

file_name = 'Q&A.csv'
output_file_name = 'Q&A_points.csv'


def get_p_number():
    player_number = int(input("How many players?"))
    if player_number == 1:
        print("Opening single player mode")
        start_1p_game()
    elif player_number in range(6):
        print(f"Opening the game for {player_number} players")
        return player_number
    elif player_number >= 6:
        print("Too many players. Game only available up to 5 players. Choose again")
        get_p_number()
    else:
        print("Incorrect input, choose a number between 1 and 5")
        get_p_number()


def create_player():
    player_name = input("What's your name?")
    return [player_name, 0]


def start_mp_game():
    num_players = get_p_number()
    player_dict = {}
    while num_players:
        player_list = create_player()
        player_dict["name"] = player_list[0]
        player_dict["points"] = player_list[1]
        num_players -= 1
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
                player_info[1] += 1
    save_results(output_file_name, player_info)
    show_results(player_info)
