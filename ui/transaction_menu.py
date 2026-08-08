from utils.input import get_menu_choice
import utils.formatter as uti_for
from utils.input import add_transaction_ui
import services.transaction_service as ser_trx
from ui.all_menus import TRANSACTION_MENU
def display_transaction_menu():
    while True:
        print("\n" + "=" * 50)
        print("      Transaction Menu")
        print("="* 50)

        for index,value in enumerate(TRANSACTION_MENU,start=1):
            print(f"{index}. {value}")

        choice = get_menu_choice(1,len(TRANSACTION_MENU))

        if choice ==1:
            add_transaction_ui("Income")
        
        elif choice ==2:
            add_transaction_ui("Expense")
        
        elif choice ==3:
            print("\n Edit Transaction - Coming Soon")
        
        elif choice ==4:
            print("\n Delete Transaction - Coming Soon")
        
        elif choice ==5:

            transactions = ser_trx.view_transactions()

            if not transactions:
                print("\nNo transactions found")
            else:
                for index,transaction in enumerate(transactions,start=1):
                    uti_for.display_front_header(index)
            
                    uti_for.display_transaction_format(transaction)
        
        elif choice ==6:
            print("\n Return to Main Menu")
            break