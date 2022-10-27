import requests
import json
from univFunc import formatArgs

class contact:
    def __init__(self, data, Client):
        self.Client = Client
        self.data = data
        self.address = data['address']
        self.address2 = data['address2']
        self.birthdate = data['birthdate']
        self.city = data['city']
        self.country = data['country']
        self.county = data['county']
        self.email = data['email']
        self.email_authorized = data['email_authorized']
        self.email_opted_in = data['email_opted_in']
        self.email_verified = data['email_verified']
        self.id = data['id']
        self.inserted_at = data['inserted_at']
        self.name_first = data['name_first']
        self.name_last = data['name_last']
        self.name_suffix = data['name_suffix']
        self.name_title = data['name_title']
        self.phone_home = data['phone_home']
        self.phone_mobile = data['phone_mobile']
        self.phone_work = data['phone_work']
        self.post_code = data['post_code']
        self.sms_authorized = data['sms_authorized']
        self.sms_opted_in = data['sms_opted_in']
        self.sms_verified = data['sms_verified']
        self.state = data['state']
        self.timezone = data['timezone']
        self.unique_id = data['unique_id']
        self.unsubscribe_email = data['unsubscribe_email']
        self.unsubscribe_sms = data['unsubscribe_sms']
        self.updated_at = data['updated_at']

        self.accounts = None

    def update(self, name_title = None, name_first = None, name_last = None, name_suffix = None,
                    address = None, address2 = None, city = None, state = None, county = None, country = None, post_code = None,
                    timezone = None, email = None, phone_home = None, phone_mobile = None, phone_work = None,
                    email_verified = None, email_opted_in = None, email_authorized = None,
                    sms_verified = None, sms_opted_in = None, sms_authorized = None, unsubscribe_email = None, birthdate = None):
        payload = formatArgs(locals())
        self.req = requests.put(f'https://api.digitalonboarding.com/v1/contacts/{self.id}', headers=self.Client.default_headers, data=payload)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self
    
    def delete(self):
        self.req = requests.delete(f'https://api.digitalonboarding.com/v1//contacts/{self.id}', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        return self

    def updateObjective(self, objective_id, status):
        payload = {
            "status":status
        }
        self.req = requests.put(f'https://api.digitalonboarding.com/v1/contacts/{self.id}/objectives/{objective_id}', headers=self.Client.default_headers, data=payload)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self

class contacts:
    def __init__(self, Client):
        self.Client = Client
        self.contact_id = None
        self.req = None
        self.status_code = None
        self.data = None

        self.doAccounts = None

    def create(self = None, unique_id = None, name_title = None, name_first = None, name_last = None, name_suffix = None,
                    address = None, address2 = None, city = None, state = None, county = None, country = None, post_code = None,
                    timezone = None, email = None, phone_home = None, phone_mobile = None, phone_work = None,
                    email_verified = None, email_opted_in = None, email_authorized = None,
                    sms_verified = None, sms_opted_in = None, sms_authorized = None, unsubscribe_email = None):
        payload = {
            "unique_id":unique_id,
            "name_title":name_title,
            "name_first":name_first,
            "name_last":name_last,
            "name_suffix":name_suffix,
            "address":address,
            "address2":address2,
            "city":city,
            "state":state,
            "county":county,
            "country":country,
            "post_code":post_code,
            "timezone":timezone,
            "email":email,
            "phone_home":phone_home,
            "phone_mobile":phone_mobile,
            "phone_work":phone_work,
            "email_verified":email_verified,
            "email_opted_in":email_opted_in,
            "email_authorized":email_authorized,
            "sms_verified":sms_verified,
            "sms_opted_in":sms_opted_in,
            "sms_authorized":sms_authorized,
            "unsubscribe_email":unsubscribe_email
        }
        self.req = requests.post('https://api.digitalonboarding.com/v1/contacts', headers=self.Client.default_headers, data=payload)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self

    def bulk_upsert(self, bulk_contacts):
        records = []
        for contact in bulk_contacts:
            records.append(formatArgs(contact, False))
        batch_api = {
            "type": "contact",
            "source": "api",
            "records": records
        }
        self.req = requests.post(f'https://api.digitalonboarding.com/v1/batches', headers=self.Client.default_headers, data=json.dumps(batch_api))

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self.status_code

    def get(self):
        self.req = requests.get(f'https://api.digitalonboarding.com/v1//contacts/{self.contact_id}', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return contact(self.data, self.Client)

    def update(self, name_title = None, name_first = None, name_last = None, name_suffix = None,
                    address = None, address2 = None, city = None, state = None, county = None, country = None, post_code = None,
                    timezone = None, email = None, phone_home = None, phone_mobile = None, phone_work = None,
                    email_verified = None, email_opted_in = None, email_authorized = None,
                    sms_verified = None, sms_opted_in = None, sms_authorized = None, unsubscribe_email = None, birthdate = None):
        payload = formatArgs(locals())
        self.req = requests.put(f'https://api.digitalonboarding.com/v1/contacts/{self.contact_id}', headers=self.Client.default_headers, data=payload)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self
    
    def delete(self):
        self.req = requests.delete(f'https://api.digitalonboarding.com/v1//contacts/{self.contact_id}', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        return self

    def list(self, limit=20, offset=0, sort_col='inserted_at', sort_dir='desc', search_term=None):
        url = f'https://api.digitalonboarding.com/v1/contacts?limit={limit}&offset={offset}&sort_column={sort_col}&sort_direction={sort_dir}'
        if search_term:
            url += f'&search={search_term}'
        self.req = requests.get(url, headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_contacts = []
        for x in self.data:
            list_contacts.append(contact(x, self.Client))
        return list_contacts
        
    def accounts(self, account_id = None):
        if self.doAccounts == None:
            from do.doAccounts import accounts
            self.doAccounts = accounts(self.Client, self.contact_id, account_id)
        if account_id:
            self.doAccounts.account_id = account_id
        return self.doAccounts

    def objectives(self):
        url = f'https://api.digitalonboarding.com/v1/contacts/{self.contact_id}/accounts'
        self.req = requests.get(url, headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self.data

    def updateObjective(self, objective_id, status):
        payload = {
            "status":status
        }
        self.req = requests.put(f'https://api.digitalonboarding.com/v1/contacts/{self.contact_id}/objectives/{objective_id}', headers=self.Client.default_headers, data=json.dumps(payload))

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return self