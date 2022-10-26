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
        self.user_id = f"{self.request.json()['user_id']}"
        self.default_headers = {
            'accept': 'application/json',
            'Content-Type':'application/json; charset=utf-8',
            'authorization': self.auth_token
        }
        self.doContacts = None
        self.doObjectives = None
        self.doPages = None
        self.doMessages = None
        self.doCampaigns = None
        self.doJourneys = None

    def getMessagePerfomance(self, template_id, start=None, end=None):
        url = f'https://api.digitalonboarding.com/v1/templates/{template_id}/insights/message-performance'
        if start and end:
            url = f'https://api.digitalonboarding.com/v1/templates/{template_id}/insights/message-performance?start_date={start}&end_date={end}'
        return requests.get(url=url, headers=self.default_headers, timeout=300)

    def campaigns(self, campaign_id = None):
        if self.doCampaigns == None:
            from do.doCampaigns import campaigns
            self.doCampaigns = campaigns(self, campaign_id)
        if campaign_id:
            self.doCampaigns.campaign_id = campaign_id
        return self.doCampaigns

    def contacts(self, contact_id = None):
        if self.doContacts == None:
            from do.doContacts import contacts
            self.doContacts = contacts(self)
        if contact_id:
            self.doContacts.contact_id = contact_id
        return self.doContacts

    def journeys(self, journey_id = None):
        if self.doMessages == None:
            from do.doJourneys import journeys
            self.doJourneys = journeys(self)
        if journey_id:
            self.doJourneys.journey_id = journey_id
        return self.doJourneys

    def messages(self, message_id = None):
        if self.doMessages == None:
            from do.doMessages import messages
            self.doMessages = messages(self)
        if message_id:
            self.doMessages.page_id = message_id
        return self.doMessages

    def objectives(self, objective_id = None):
        if self.doObjectives == None:
            from do.doObjectives import objectives
            self.doObjectives = objectives(self)
        if objective_id:
            self.doObjectives.objective_id = objective_id
        return self.doObjectives

    def pages(self, page_id = None):
        if self.doPages == None:
            from do.doPages import pages
            self.doPages = pages(self)
        if page_id:
            self.doPages.page_id = page_id
        return self.doPages