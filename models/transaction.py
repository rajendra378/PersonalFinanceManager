def create_transaction(ids,amount,category,description,date,transaction_type,mode):
    """
    Create and return a transaction dectionary.
    """
    # print("create_transaction  called in models/transaction.py")
    return {
        "id":ids,
        "amount":amount,
            "category":category,
            "description":description,
            "date":date,
            "type":transaction_type,
            "mode":mode,    
    }