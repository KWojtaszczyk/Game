from question_loader import get_questions_ready, save_results, ask_question
from input_and_check import get_answer_to_question, check_the_answer, get_q_number, create_player

file_name = 'Q&A.csv'
output_file_name = 'Q&A_points.txt'


def start_1p_game():

    num_questions = get_q_number()
    chosen_questions = get_questions_ready(num_questions)
    chosen_name = create_player()
    sp_user = [chosen_name, 0]
    quiz_game(sp_user, chosen_questions)


def quiz_game(user_list, chosen_questions):
    for i in chosen_questions:
        ask_question(i)
        player_answer = get_answer_to_question()
        if check_the_answer(player_answer, i):
            user_list[1] += 1
    user_profile = str(f"{user_list[0]} scored {user_list[1]} points")
    save_results(output_file_name, user_profile)
    print(user_profile)





