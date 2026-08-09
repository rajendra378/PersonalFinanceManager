import repository.transaction_repository as repo_trx


def search_transaction_by_id(search_id):

    transactions = repo_trx.get_all_transactions()

    return list(
        filter(lambda transaction:transaction["id"] == search_id,transactions)
        )

def search_transaction_by_category(category):
    transactions = repo_trx.get_all_transactions()

    return list(filter(
        lambda transaction: category.lower() in transaction["category"].lower() ,transactions
    ))

def search_transaction_by_type(transaction_types):

    transactions = repo_trx.get_all_transactions()

    for i in transactions:
        return list(
            filter(lambda transaction:transaction["transaction_type"].lower() == transaction_types.lower(),transactions)
            )

def search_transaction_by_mode(mode):
    transactions = repo_trx.get_all_transactions()

    return list(
            filter(lambda transaction:transaction["mode"].lower() == mode.lower(),transactions)
            )

def search_transaction_by_date(transaction_date):
    transactions = repo_trx.get_all_transactions()

    return list(
            filter(lambda transaction:transaction["date"] == transaction_date,transactions)
            )

def search_transaction_by_amount(transaction_amount):
    transactions = repo_trx.get_all_transactions()

    return list(
            filter(lambda transaction:transaction["amount"] == float(transaction_amount),transactions)
            )

def search_transaction_by_description(search_description):
    transactions = repo_trx.get_all_transactions()

    return list(filter(
        lambda transaction: search_description.lower() in transaction["description"].lower() ,transactions
    ))