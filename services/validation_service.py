def validate_amount(amount):
    if amount > 0:
        return amount
    raise ValueError("Amount must be greater than zero.")

def validate_id(ids):
    if ids > 0:
        return ids
    raise ValueError("ID must be greater than zero.")
