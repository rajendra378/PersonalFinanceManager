def display_transaction_format(transaction):
    for key,value in transaction.items():
        print(f"{key:<12}:{value}")

def display_front_header(index):
    print("="*50)
    print(" "*10+"Transactions")
    print("="*50)
    print(f"Transaction #{index}")
    print("="*50)