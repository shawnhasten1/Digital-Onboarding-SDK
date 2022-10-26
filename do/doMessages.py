import requests

class message:
    def __init__(self, data, Client):
        self.Client = Client
        self.data = data

        self._type = data['_type']
        self.body_preview = data['body_preview']
        self.content_name = data['content_name']
        self.id = data['id']
        self.is_archived = data['is_archived']
        self.objective_id = data['objective_id']
        self.team_id = data['team_id']
        self.type = data['type']

class messages:
    def __init__(self, Client, objective_id = None, message_id = None):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.objective_id = objective_id
        self.message_id = message_id

    def list(self, objective_id = None, message_id = None):
        url = 'https://api.digitalonboarding.com/v1/content-library?content_types[]=sms&content_types[]=email&is_archived=false'
        if objective_id:
            self.objective_id = objective_id
        if self.objective_id:
            url += f'&objective={self.objective_id}'
        self.req = requests.get(url, headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_messages = []
        for x in self.data:
            list_messages.append(message(x, self.Client))
        return list_messages