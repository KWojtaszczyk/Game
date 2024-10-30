import random
from question_loader import load_questions, save_results, ask_question, get_answer_to_question, check_the_answer

file_name = 'Q&A.csv'
output_file_name = 'Q&A_points.txt'


def start_1p_game():

    chosen_name = input("What's your name?\n")
    sp_user = [chosen_name, 0]
    quiz_game(sp_user)


def quiz_game(user_list):
    questions = (load_questions(file_name))
    random.shuffle(questions)
    for i in questions:
        ask_question(i)
        player_answer = get_answer_to_question()
        if check_the_answer(player_answer, i) == 1:
            user_list[1] += 1
    user_profile = str(f"{user_list[0]} scored {user_list[1]} points")
    save_results(output_file_name, user_profile)
    print(user_profile)





