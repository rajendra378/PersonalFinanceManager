from ui.all_menus import MAIN_MENU

def display_main_menu():
    print("\n" + "=" * 50)
    print("     Personal Finance Manager")
    print("=" * 50)

    for index,value in enumerate(MAIN_MENU,start=1):

        print(f"{index}. {value}")
