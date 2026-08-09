def display_transaction_format(transaction):
    for key,value in transaction.items():
        print(f"{key:<12}:{value}")

def display_front_header(index):
    print("="*50)
    print(" "*10+"Transactions")
    print("="*50)
    print(f"Transaction #{index}")
    print("="*50)

def display_transaction(transactions):
    for index,transaction in enumerate(transactions,start=1):
        display_front_header(index)
        
        display_transaction_format(transaction)