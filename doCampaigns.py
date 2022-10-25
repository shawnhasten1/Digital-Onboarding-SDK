import requests

class campaign:
    def __init__(self, data, Client):
        self.Client = Client
        self.data = data

        self.id = data['id']
        self.key = data['key']
        self.name = data['name']

class campaigns:
    def __init__(self, Client):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.campaign_id = None

    def list(self):
        self.req = requests.get('https://api.digitalonboarding.com/v1/campaigns', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_campaigns = []
        for x in self.data:
            list_campaigns.append(campaign(x, self.Client))
        return list_campaigns