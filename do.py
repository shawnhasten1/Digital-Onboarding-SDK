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
        self.doContacts = None
        self.doObjectives = None
        self.doPages = None
        self.doMessages = None

    def getMessagePerfomance(self, template_id, start=None, end=None):
        url = f'https://api.digitalonboarding.com/v1/templates/{template_id}/insights/message-performance'
        if start and end:
            url = f'https://api.digitalonboarding.com/v1/templates/{template_id}/insights/message-performance?start_date={start}&end_date={end}'
        return requests.get(url=url, headers=self.default_headers, timeout=300)

    def contacts(self, contact_id = None):
        if self.doContacts == None:
            from doContacts import contacts
            self.doContacts = contacts(self)
        if contact_id:
            self.doContacts.contact_id = contact_id
        return self.doContacts

    def objectives(self, objective_id = None):
        if self.doObjectives == None:
            from doObjectives import objectives
            self.doObjectives = objectives(self)
        if objective_id:
            self.doObjectives.objective_id = objective_id
        return self.doObjectives

    def pages(self, page_id = None):
        if self.doPages == None:
            from doPages import pages
            self.doPages = pages(self)
        if page_id:
            self.doPages.page_id = page_id
        return self.doPages

    def messages(self, message_id = None):
        if self.doMessages == None:
            from doMessages import messages
            self.doMessages = messages(self)
        if message_id:
            self.doMessages.page_id = message_id
        return self.doMessages