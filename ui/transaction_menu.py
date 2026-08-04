from utils.input import get_menu_choice
import utils.formatter as uti_for
import services.transaction_service as ser_trx

def transaction_menu():
    while True:
        print("\n" + "=" * 50)
        print("      Transaction Menu")
        print("="* 50)

        print("1. Add Income")
        print("2. Add Expense")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. View Transaction")
        print("6. Back")

        choice = get_menu_choice(1,6)

        if choice ==1:
            ser_trx.add_income(
                amount = 500000,
                category = "Salery",
                description = "July Salary",
                date = "2026-08-03",
                mode = "Bank Transfer")
            print("\n Income added successfully.")
        
        elif choice ==2:
            print("\n Add Expense - Coming Soon")
        
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
            
                    uti_for.idisplay_transaction_format(transaction)
        
        elif choice ==6:
            print("\n Return to Main Menu - Coming Soon")
            break