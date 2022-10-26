import requests
import json

class journey:
    def __init__(self, data, Client):
        self.Client = Client
        self.data = data

        self.account_id = data['account_id']
        self.analytics_cache = data['analytics_cache']
        self.completion_verified_at = data['completion_verified_at']
        self.contact = data['contact']
        self.id = data['id']
        self.inserted_at = data['inserted_at']
        self.owner = data['owner']
        self.reward_dispensed_at = data['reward_dispensed_at']
        self.slug = data['slug']
        self.source = data['source']
        self.template = data['template']
        self.template_id = data['template_id']
        self.updated_at = data['updated_at']
        self.web_client_url = data['web_client_url']
    
    def delete(self):
        self.req = requests.delete(f'https://api.digitalonboarding.com/v1/templates/{self.template_id}/journeys/{self.id}', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        return self

class journeys:
    def __init__(self, Client, campaign_id = None, journey_id = None):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.campaign_id = campaign_id
        self.journey_id = journey_id

        self.doContact = None

        self.owner_id = self.Client.user_id

    def get(self):
        self.req = requests.get(f'https://api.digitalonboarding.com/v1/journeys/{self.journey_id}', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return journey(self.data, self.Client)

    def create(self, unique_id, contact_details = {}):
        payload = {
            "source":"direct",
            "owner_id":self.owner_id,
            "unique_id":unique_id,
            "contact":{
                "source":"direct",
                "owner_id":self.owner_id,
                "unique_id":unique_id
            }
        }
        for detail in contact_details:
            payload[detail] = contact_details[detail]
            payload['contact'][detail] = contact_details[detail]
        self.req = requests.post(f'https://api.digitalonboarding.com/v1/templates/{self.campaign_id}/journeys', headers=self.Client.default_headers, data=json.dumps(payload))

        self.status_code = self.req.status_code
        self.data = self.req.json()
        return journey(self.data, self.Client)

    def delete(self):
        self.req = requests.delete(f'https://api.digitalonboarding.com/v1/templates/{self.campaign_id}/journeys/{self.journey_id}', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        return self

    def list(self, limit=20, offset=0, sort_col='inserted_at', sort_dir='desc', search_term=None):
        url = f'https://api.digitalonboarding.com/v1/templates/{self.campaign_id}/journeys?limit={limit}&offset={offset}&sort_column={sort_col}&sort_direction={sort_dir}'
        if search_term:
            url = f'&search={search_term}'
        self.req = requests.get(url, headers=self.Client.default_headers)
        #print(f'https://api.digitalonboarding.com/v1/templates/{self.campaign_id}/journeys?limit={limit}&offset={offset}&sort_column={sort_col}&sort_direction={sort_dir}&search={search_term}')

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_journeys = []
        for data in self.data:
            list_journeys.append(journey(data, self.Client))
        return list_journeys

    def analytics(self):
        self.req = requests.get(f'https://api.digitalonboarding.com/v1/analytics?journey_id={self.journey_id}&preload[]=page', headers=self.Client.default_headers)
        return self.req.json()

    def contact(self):
        self.req = requests.get(f'https://api.digitalonboarding.com/v1/journeys/{self.journey_id}', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()

        from do.doContacts import contact
        return contact(self.data['contact'], self.Client)