import datetime
from services import transaction_service as ser_trx
from services import validation_service as ser_val


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

def get_amount():
    while True:
        try:
            amount = float(input("Enter amount : "))
            ser_val.validate_amount(amount)
            return amount
        except ValueError as e:
            message = str(e)
            if "could not convert" in message:
                print("Enter a valid number.")
            else:
                print(f"{message}")
                

def get_category():
    while True:
        try:
            category = input("Enter Category : ").strip()
            if category == "":
                raise ValueError("Category can not be Empty Value")
            return category
        except ValueError as e:
            print(e)

def get_description():
    description = input("Enter Discription : ")
    return description

def get_date():
    date = input("enter date : ").strip()
    if date == "":
        date = datetime.date.today().isoformat()
    return date

def get_transaction_mode(transaction_type):

    if transaction_type == "Expense":
        transaction_mode = ["Cash","UPI", "Bank Transfer", "Cheque", "Credit Card", "Debit Card", "Other"]
    else:
        transaction_mode = ["Cash","UPI", "Bank Transfer", "Cheque", "Other"]
    print("Mode of Transaction: ")

    for i,value in enumerate (transaction_mode,start=1):
        print(f"{i}. {value}")
        
    choice = get_menu_choice(1,len(transaction_mode))

    return transaction_mode[choice-1]
def add_transaction_ui(transaction_type):
    amount = get_amount()
    category = get_category()
    description = get_description()
    date = get_date()
    transaction_mode = get_transaction_mode(transaction_type)
    # print("add_transaction_ui called")
    transaction = ser_trx.add_transaction(amount,category,description,date,transaction_mode,transaction_type)
    

    