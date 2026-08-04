import models.transaction as mod_trs
import repository.transaction_repository as repo_trx


def add_income(amount,
               category,
               description,
               date,
               mode):
    transaction = mod_trs.create_transaction(amount=amount,
                                     category=category,
                                     description=description,
                                     date=date,
                                     transaction_type = "income",
                                     mode = mode)
    repo_trx.save_transaction(transaction)

def view_transactions():
    return repo_trx.get_all_transactions()

