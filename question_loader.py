import csv


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


def get_answer_to_question():
    answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

    if answer not in ['A', 'B', 'C', 'D']:
        print("Invalid answer.")
        get_answer_to_question()

    return answer


def check_the_answer(answer, row):
    correct_answer = row[5]
    if answer == correct_answer:
        return 1
    else:
        return 0
