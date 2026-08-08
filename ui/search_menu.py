from utils.input import get_menu_choice

def transaction_menu():
    while True:
        print("\n" + "=" * 50)
        print("      Search Menu")
        print("="* 50)

        print("1. ID")
        print("2. Category")
        print("3. Type")
        print("4. Mode")
        print("5. Date")
        print("6. amount")
        print("7. Description")

        choice = get_menu_choice(1,7)
        if choice ==1:
            add_transaction_ui("Income")
                
        elif choice ==2:
            add_transaction_ui("Expense")
                
        elif choice ==3:
            print("\n Edit Transaction - Coming Soon")
                
        elif choice ==4:
            print("\n Delete Transaction - Coming Soon")
                
        elif choice ==6:
                    print("\n Return to Main Menu - Coming Soon")
                    break