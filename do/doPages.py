import requests

class page:
    def __init__(self, data, Client):
        self.Client = Client
        self.data = data

        self._type = data['_type']
        self.benchmark = data['benchmark']
        self.completion_condition = data['completion_condition']
        self.completion_message = data['completion_message']
        self.content = data['content']
        self.content_block_status = data['content_block_status']
        self.content_name = data['content_name']
        self.css = data['css']
        self.cta = data['cta']
        self.hide_when_complete = data['hide_when_complete']
        self.id = data['id']
        self.is_archived = data['is_archived']
        self.is_live = data['is_live']
        self.is_shared = data['is_shared']
        self.layout_basis = data['layout_basis']
        self.navigation_title = data['navigation_title']
        self.new_slug = data['new_slug']
        self.objective_id = data['objective_id']
        self.old_slug = data['old_slug']
        self.slug = data['slug']
        self.styles = data['styles']
        self.team_id = data['team_id']
        self.updated_at = data['updated_at']

class pages:
    def __init__(self, Client, objective_id = None, page_id = None):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.objective_id = objective_id
        self.page_id = page_id

    def list(self, objective_id = None, page_id = None):
        url = 'https://api.digitalonboarding.com/v1/pages?is_archived=false'
        if objective_id:
            self.objective_id = objective_id
        if self.objective_id:
            url += f'&objective={self.objective_id}'
        self.req = requests.get(url, headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_pages = []
        for x in self.data:
            list_pages.append(page(x, self.Client))
        return list_pages