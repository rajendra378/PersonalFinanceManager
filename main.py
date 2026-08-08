from ui.main_menu import display_main_menu
import ui.transaction_menu as ui_trx
import ui.search_menu as ui_search
from utils.input import get_menu_choice

def main():
    while True:
        display_main_menu()

        choice = get_menu_choice(1,6)

        if choice == 1:
            ui_trx.display_transaction_menu()

        elif choice == 3:
            ui_search.search_menu()
        elif choice == 6:
            print("\n Thank you for using Personal Finance Manager!")
            break
        else:
            print("\nFeature coming soon...")

if __name__ == "__main__":
    main()