import requests
import json
from univFunc import formatArgs

class account:
    def __init__(self, data, Client):
        self.Client = Client
        self.data = data

        self.id = data['account']['id']
        self.meta_public = data['account']['meta_public']
        self.nickname = data['account']['nickname']
        self.product = data['account']['product']

class accounts:
    def __init__(self, Client, contact_id = None, account_id = None):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.contact_id = contact_id
        self.account_id = account_id

    def upsert(self, account_number = None, contact_unique_id = None, product_code = None, product_type = None,
                product_name = None, product_description = None, contact_role = None, micr = None, routing_number = None,
                opened_date = None, closed_date = None, nickname = None, balance = None,
                number_transactions_last_30_days = None, total_amount_last_30_days = None,
                status_code = None, adverse_status = None, channel_opened = None, closed_reason = None,
                credit_card_activation = None, last_mobile_pay_transaction = None, last_statement_balance = None,
                last_transaction_amount = None, last_transaction_date = None, apy = None, charge_off = None,
                payment_due_date = None, in_person_deposit_check_date = None, payment_frequency = None,
                payment_method = None, loan_payment = None, loan_payoff_date = None, loan_principal = None,
                loan_term = None, maturity_date = None, last_debit_card_transaction = None,
                last_mobile_pay_amount = None, remote_deposit_last_30_days = None, meta_public = {},
                meta_private = {}):
        if account_number == None:
            raise ValueError("account_number is required to create an account")
        if contact_unique_id == None:
            raise ValueError("contact.unique_id is required to create an account")
        if product_code == None:
            raise ValueError("product_code is required to create an account")
        if product_type == None:
            raise ValueError("product_type is required to create an account")
        payload = formatArgs(locals(), False)
        batch_api = {
            "type": "account",
            "source": "api",
            "records": []
        }
        batch_api['records'].append(payload)
        self.req = requests.post(f'https://api.digitalonboarding.com/v1/batches', headers=self.Client.default_headers, data=json.dumps(batch_api))

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self.status_code

    def bulk_upsert(self, bulk_accounts):
        records = []
        for account in bulk_accounts:
            records.append(formatArgs(account, False))
        batch_api = {
            "type": "account",
            "source": "api",
            "records": records
        }
        self.req = requests.post(f'https://api.digitalonboarding.com/v1/batches', headers=self.Client.default_headers, data=json.dumps(batch_api))

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self.status_code

    def list(self):
        url = f'https://api.digitalonboarding.com/v1/contacts/{self.contact_id}/accounts'
        self.req = requests.get(url, headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_accounts = []
        for data in self.data:
            list_accounts.append(account(data, self.Client))
        return list_accounts