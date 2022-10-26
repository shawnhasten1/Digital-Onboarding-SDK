import requests

class objective:
    def __init__(self, data, Client):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.id = data['id']
        self.key = data['key']
        self.name = data['name']

class objectives:
    def __init__(self, Client, objective_id = None):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.objective_id = objective_id

        self.doPages = None
        self.doMessages = None

    def list(self):
        self.req = requests.get('https://api.digitalonboarding.com/v1/objectives', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_objectives = []
        for x in self.data:
            list_objectives.append(objective(x, self.Client))
        return list_objectives

    def pages(self, page_id = None):
        if self.doPages == None:
            from doPages import pages
            self.doPages = pages(self.Client, self.objective_id, page_id)
        if page_id:
            self.doPages.page_id = page_id
        return self.doPages

    def messages(self, message_id = None):
        if self.doMessages == None:
            from doMessages import messages
            self.doMessages = messages(self.Client, self.objective_id, message_id)
        if message_id:
            self.doMessages.page_id = message_id
        return self.doMessages