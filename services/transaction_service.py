import models.transaction as mod_trs
import repository.transaction_repository as repo_trx



def add_transaction(amount,
               category,
               description,
               date,
               mode,
               transaction_type):
    ids = repo_trx.get_next_transaction_id()
    # print(f"{ids} it is called in add_transaction service") 
    transaction = mod_trs.create_transaction(
    ids=ids,
    amount=amount,
    category=category,
    description=description,
    date=date,
    transaction_type = transaction_type,
    mode = mode)
    # print("save_transaction called in services/transaction_service.py")
    repo_trx.save_transaction(transaction)
    return transaction

def view_transactions():
    return repo_trx.get_all_transactions()

