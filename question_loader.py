import csv
import random

file_name = 'Q&A.csv'


def load_questions(question_file):
    with open(question_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        questions_list = list(csv_reader)
    return questions_list


def save_results(result_file, user_profile):
    with open(result_file, mode='a', encoding='utf-8') as output_file:
        output_file.write(f"\n{user_profile}")
    print(f"Results saved to {result_file}")


def ask_question(row):
    print(f"Question: {row[0]}")
    print(f"A) {row[1]}")
    print(f"B) {row[2]}")
    print(f"C) {row[3]}")
    print(f"D) {row[4]}")


def get_questions_ready(question_choice):
    questions = load_questions(file_name)
    random.shuffle(questions)
    numbered_questions = questions[:question_choice]
    return numbered_questions
