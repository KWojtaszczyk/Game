from menu_func import show_menu, choice

# Create a main entry to the app


def main():


    # show menu options
    show_menu()
    chosen_option = input("What do you want to do?\n")

    # user chooses an option
    choice(chosen_option)


if __name__ == "__main__":
    main()
