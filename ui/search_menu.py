import utils.input as uti_in
import utils.formatter as uti_for
from ui.all_menus import SEARCH_MENU
import services.search_service as ser_search

def search_menu():
    while True:
        print("\n" + "=" * 50)
        print("      Search Menu")
        print("="* 50)

        for index,value in enumerate(SEARCH_MENU,start=1):
             print(f"{index}. {value}")

        choice = uti_in.get_menu_choice(1,len(SEARCH_MENU))
        if choice ==1:
            id = uti_in.get_id()

            transactions = ser_search.search_transaction_by_id(id)
            uti_for.display_transaction(transactions)
                
        elif choice ==2:
            category = uti_in.get_category()

            transactions = ser_search.search_transaction_by_description_or_category(category)

            uti_for.display_transaction(transactions)

        elif choice ==3:
            transaction_type = uti_in.get_transaction_type_for_search()

            transactions = ser_search.search_transaction_by_type(transaction_type)

            uti_for.display_transaction(transactions)
                
        elif choice ==4:
            amount = uti_in.get_amount()

            transactions = ser_search.search_transaction_by_amount(amount)

            uti_for.display_transaction(transactions)

                
        elif choice ==5:
            date = uti_in.get_date()

            transactions = ser_search.search_transaction_by_date(date)

            uti_for.display_transaction(transactions)

        elif choice ==6:
            description = uti_in.get_description()

            transactions = ser_search.search_transaction_by_description_or_category(description)

            uti_for.display_transaction(transactions)
                
        elif choice ==7:
            mode = uti_in.get_transaction_mode_for_search()
            transactions = ser_search.search_transaction_by_mode(mode)

            uti_for.display_transaction(transactions)

        elif choice == 8:
                    print("\n Return to Main Menu")
                    break
