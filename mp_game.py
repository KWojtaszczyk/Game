from question_loader import get_questions_ready, save_results, ask_question
from input_and_check import get_answer_to_question, check_the_answer, get_p_number, get_q_number, create_player


output_file_name = 'Q&A_points.txt'


def start_mp_game():
    num_players = get_p_number()
    num_questions = get_q_number()
    chosen_questions = get_questions_ready(num_questions)
    player_dict = {}
    for i in range(num_players):
        print(f"Player {i + 1}")
        player_dict[create_player()] = 0
    mp_quiz_game(player_dict, chosen_questions)


def mp_quiz_game(player_info, question_dict):
    for i in question_dict:
        for j in player_info.keys():
            print(f"{j}'s turn:")
            ask_question(i)
            player_answer = get_answer_to_question()
            if check_the_answer(player_answer, i):
                player_info[j] += 1
    for k in player_info.keys():
        user_profile = str(f"{k} scored {player_info[k]} points")
        save_results(output_file_name, user_profile)
        print(user_profile)
