import requests
import json

class Client:
    def __init__(self, url, user, password):
        self.url = url
        self.user = user
        self.request_headers = {
            'origin':url,
            'accept':'application/json',
            'content-type':'application/json'
        }
        payload = json.dumps({
            "email": self.user,
            "grant_type": "password",
            "password": password
        })
        self.request = requests.post('https://api.digitalonboarding.com/oauth2/token', headers=self.request_headers, data=payload)
        self.auth_token = f"Bearer {self.request.json()['access_token']}"
        self.default_headers = {
            'accept': 'application/json',
            'authorization': self.auth_token
        }
        self.ddContacts = None

    def getMessagePerfomance(self, template_id, start=None, end=None):
        url = f'https://api.digitalonboarding.com/v1/templates/{template_id}/insights/message-performance'
        if start and end:
            url = f'https://api.digitalonboarding.com/v1/templates/{template_id}/insights/message-performance?start_date={start}&end_date={end}'
        return requests.get(url=url, headers=self.default_headers, timeout=300)

    def contacts(self, contact_id = None):
        if self.ddContacts == None:
            from doContacts import contacts
            self.ddContacts = contacts(self)
        if contact_id:
            self.ddContacts.contact_id = contact_id
        return self.ddContacts