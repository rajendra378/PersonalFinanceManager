import json

TRANSACTION_FILE = "transactions.json"


def get_all_transactions():
    with open(TRANSACTION_FILE, "r") as file:
        data = json.load(file)

    return data["transactions"]

def save_transactions(transactions):
    data = {
        "transactions":transactions
    }
    with open(TRANSACTION_FILE,"w") as file:
        json.dump(data,file,indent=4)
    print("\nTransaction saved successfully...\n")

def get_next_transaction_id():
    transactions = get_all_transactions()
    if not transactions:
        return 1
    """
    
    This line extracts the id from every transaction, finds the largest ID using max(), and returns the next available ID by adding 1.
    
    """
    return max(transaction["id"] for transaction in transactions)+1

def save_transaction(transaction):
    transactions = get_all_transactions()
    transactions.append(transaction)
    save_transactions(transactions)



# def find_by_category()
    
# def find_by_mode()

# def find_by_type()

# def delete_transaction()

# def update_transaction()


