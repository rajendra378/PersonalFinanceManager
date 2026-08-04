def create_transaction(amount,category,description,date,transaction_type,mode):
    """
    Create and return a transaction dectionary.
    """
    return {
        "amount":amount,
            "category":category,
            "description":description,
            "date":date,
            "type":transaction_type,
            "mode":mode,    
    }