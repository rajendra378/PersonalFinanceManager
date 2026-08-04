def get_menu_choice(min_choice,max_choice):

    """
    Prompt the user until a valid menu option is entered.
    """

    while True:
        choice = input("\n Enter your choice: ").strip()

        if not choice:
            print("Input cannot be empty.")
            continue
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue
        choice = int(choice)

        if choice < min_choice or choice > max_choice:
            print(f"Please enter a number between {min_choice} and {max_choice}.")
            continue

        return choice
    
    