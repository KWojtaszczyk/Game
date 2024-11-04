

def create_player():
    player_name = input("What's your name?\n")
    return player_name


def get_p_number():
    while True:
        input_str = input("How many players? 2-5\n")

        if not input_str.isdigit():
            print("Incorrect input")
            continue

        player_number = int(input_str)

        if player_number == 1:
            print("Too few players")
        elif 2 <= player_number <= 5:
            print(f"Opening the game for {player_number} players")
            return player_number
        else:
            print("Too many players. Game only available up to 5 players. Choose again")


def get_q_number():
    while True:
        q_number = input("How many questions do you want to answer in this game? 1-15: \n")

        if not q_number.isdigit():
            print("Invalid input.")
            continue

        if 1 <= int(q_number) <= 15:
            return int(q_number)
        else:
            print("Invalid input. Please enter a number between 1 and 15.")


def get_answer_input():
    answer = input("Enter your answer (A, B, C, or D): \n").strip().upper()
    return answer


def get_answer_to_question():
    correct_answer = get_answer_input()

    while correct_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid answer.")
        correct_answer = get_answer_input()

    return correct_answer


def check_the_answer(answer, row):
    correct_answer = row[5]
    return answer == correct_answer
