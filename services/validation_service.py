def validate_amount(amount):
    if amount > 0:
        return amount
    raise ValueError("Amount must be greater than zero.")