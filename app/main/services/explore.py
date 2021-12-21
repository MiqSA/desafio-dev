import pandas as pd
from app.main.config import ConnectionDB
from app.main.services.standards import Output


class Transactions():

    def __init__(self):
        self._engine = ConnectionDB().get_engine()

    def get_stores(self):
        """ This function return the stores."""
        try:
            comand_sql = f"""SELECT DISTINCT store_name FROM transactions"""
            data = pd.read_sql(comand_sql, con=self._engine)
            data = data.store_name
            return Output().return_funtion(200, data)
        except Exception as err:
            print('Error in command sql!\n', err)
            Output().return_funtion(400, None)

    def get_all_transactions(self):
        """ This function return all transactions by store."""
        try:
            comand_sql = f"""SELECT transac.transaction_value, transac.store_name, type.description
                        FROM transactions as transac, transactions_type as type
                        WHERE transac.transaction_id = type.id"""
            data = pd.read_sql(comand_sql, con=self._engine)
            transaction_by_store = data.groupby(by=['store_name', 'description']).sum()
            transaction_by_store = transaction_by_store.reset_index()
            return Output().return_funtion(200, transaction_by_store)
        except Exception as err:
            print('Error in command sql!\n', err)
            Output().return_funtion(400, None)

    def get_total(self):
        """ This function return the value transactions total."""
        try:
            comand_sql = f"""SELECT transaction_value, store_name FROM transactions"""
            data = pd.read_sql(comand_sql, con=self._engine)
            total = data.groupby(by=['store_name']).sum()
            total = total.reset_index()
            return Output().return_funtion(200, total)
        except Exception as err:
            print('Error in command sql!\n', err)
            Output().return_funtion(400, None)