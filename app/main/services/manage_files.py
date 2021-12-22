from app.main.services.standards import Output
from app.main.config import ConnectionDB
import pandas as pd
import os


class Information():
    def __init__(self, row=None):
        self.row = row

    def fields_map(self):
        try:
            information_map = {
                'transaction_id': [self.row[0]],
                'transaction_occurrence_date': [f'{self.row[1:5]}-{self.row[5:7]}-{self.row[7:9]}'],
                'transaction_value': [int(self.row[9:19]) / 100],
                'client_cpf': [self.row[19:30]],
                'client_credit_card': [self.row[30:42]],
                'transaction_hour': [int(self.row[42:48])],
                'store_owner': [self.row[48:62]],
                'store_name': [self.row[62:82]]
            }
            return information_map
        except Exception as error:
            return error

    @staticmethod
    def get_standard_transactions():
        standard = {
            'transaction_id': [],
            'transaction_occurrence_date': [],
            'transaction_value': [],
            'client_cpf': [],
            'client_credit_card': [],
            'transaction_hour': [],
            'store_owner': [],
            'store_name': []
        }
        return pd.DataFrame.from_dict(standard)

    @staticmethod
    def get_standard_transactions_type():
        description = ['Débito', 'Boleto', 'Financiamento',
                       'Crédito', 'Recebimento Empréstimo',
                       'Vendas', 'Recebimento TED', 'Recebimento DOC',
                       'Aluguel']

        mode = ['Entrada', 'Saída', 'Saída', 'Entrada',
                'Entrada', 'Entrada', 'Entrada', 'Entrada', 'Saída']

        signal = ['+', '-', '-', '+', '+', '+', '+', '+', '-']

        dict_type_transactions = {
            'description': description,
            'mode': mode,
            'signal': signal
        }

        return pd.DataFrame.from_dict(dict_type_transactions)



class CRUD():
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        file =  pd.read_csv(f'{self.filename}', header=None)
        print('File read...')
        return file

    def delete(self):
        return os.remove(f"{self.filename}")

    def save_data_in_database(self, df, table_name):
        try:
            # Check if exists table in dataframe
            comand_sql = f"""SELECT id FROM {table_name} ORDER BY ID DESC LIMIT 1"""
            read_sql = pd.read_sql(comand_sql, con=ConnectionDB().get_engine())
            last_id = int(read_sql.id[0])
            if table_name != 'transactions_type':
                print('Populating table ..')
                df.index += last_id + 1
                df.to_sql(table_name,
                          con=ConnectionDB().get_engine(),
                          if_exists='append',
                          index_label='id')
                print(f'Successfully add in {table_name}')
        except Exception as err:
            print("Table don't exists!", err)
            print('Creating table ...')
            df.to_sql(table_name,
                      con=ConnectionDB().get_engine(),
                      if_exists='replace',
                      index_label='id')
            print(f'Successfully add in {table_name}')

    def main(self):
        # Read file
        file = self.read()

        # Get transactions table
        transactions = Information().get_standard_transactions()

        try:
            # Analysing row to row
            for id_row in file.index:
                row = file[0][id_row]
                information = Information(row).fields_map()
                data_information = pd.DataFrame.from_dict(information)

                # Adding data to transactions
                transactions = transactions.append(data_information, ignore_index=True)
            pass

            # Save data in transactions table
            self.save_data_in_database(transactions, 'transactions')

            transactions_type = Information().get_standard_transactions_type()

            # Save data in transactions type table
            self.save_data_in_database(transactions_type, 'transactions_type')

            # Delete local file
            self.delete()

            return print('Operation with success')
        except Exception as err:
            # Delete local file
            self.delete()
            return print('Operation with Erro', err), 404

