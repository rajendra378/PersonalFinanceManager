import models.transaction as mod_trs
import repository.transaction_repository as repo_trx



def add_income(amount,
               category,
               description,
               date,
               mode,
               transaction_type):  
    transaction = mod_trs.create_transaction(amount=amount,
    category=category,
    description=description,
    date=date,
    transaction_type = transaction_type,
    mode = mode)
    repo_trx.save_transaction(transaction)
    return transaction

def view_transactions():
    return repo_trx.get_all_transactions()

