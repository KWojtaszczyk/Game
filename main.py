from menu_func import show_menu, choice


def main():
    while True:
        show_menu()
        chosen_option = input("What do you want to do?\n")

        choice(chosen_option)


if __name__ == "__main__":
    main()
