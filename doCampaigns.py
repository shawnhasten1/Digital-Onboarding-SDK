import requests

class campaign:
    def __init__(self, data, Client):
        self.Client = Client
        self.data = data

        self.analytics = data['analytics']
        self.custom_css = data['custom_css']
        self.template_pages = data['template_pages']
        self.theme = data['theme']
        self.targeting_group_logical_operator = data['targeting_group_logical_operator']
        self.owner_id = data['owner_id']
        self.hide_progress_ring = data['hide_progress_ring']
        self.due_date = data['due_date']
        self.id = data['id']
        self.split_testing_group_id = data['split_testing_group_id']
        self.journey_title_options = data['journey_title_options']
        self.is_reward_enabled = data['is_reward_enabled']
        self.is_cce_enabled = data['is_cce_enabled']
        self._type = data['_type']
        self.name = data['name']
        self.is_auth_required = data['is_auth_required']
        self.is_muted = data['is_muted']
        self.theme_base = data['theme_base']
        self.status = data['status']
        self.layout_basis = data['layout_basis']
        self.footer_content = data['footer_content']
        self.is_archived = data['is_archived']
        self.css = data['css']
        self.is_split_testing_group_leader = data['is_split_testing_group_leader']
        self.is_targeting_priority = data['is_targeting_priority']
        self.logo_file_id = data['logo_file_id']
        self.email_sender_name = data['email_sender_name']
        self.archived_at = data['archived_at']
        self.support_owner_options = data['support_owner_options']
        self.targeting_order = data['targeting_order']
        self.facts = data['facts']
        self.targeting_account_priority = data['targeting_account_priority']
        self.content_block_status = data['content_block_status']
        self.inserted_at = data['inserted_at']
        self.reward = data['reward']
        self.email_sender_address = data['email_sender_address']
        self.styles = data['styles']

class campaigns:
    def __init__(self, Client):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.campaign_id = None
        self.name = None

    def create(self, name, objective_details = []):
        self.name = name
        payload = {
            "template":{
                "name":self.name
            },
            "objective_rows":[]
        }
        for objective_detail in objective_details:
            objective = {
                "id":"4e1624ff-317e-4004-9e49-acefca78100a",
                "page":{
                    "_type":"page",
                    "benchmark":None,
                    "completion_condition":objective_detail.page.completion_condition,
                    "completion_message":None,
                    "content":None,
                    "content_block_status":None,
                    "content_blocks":[
                    
                    ],
                    "content_containers":[
                    
                    ],
                    "css":None,
                    "cta":None,
                    "hide_when_complete":False,
                    "id":objective_detail.page.id,
                    "is_archived":False,
                    "is_live":True,
                    "is_shared":None,
                    "layout_basis":objective_detail.page.layout_basis,
                    "navigation_title":objective_detail.page.navigation_title,
                    "new_slug":objective_detail.page.new_slug,
                    "objective_id":objective_detail.page.objective_id,
                    "old_slug":objective_detail.page.old_slug,
                    "slug":objective_detail.page.slug,
                    "styles":None,
                    "team":{
                    
                    },
                    "team_id":objective_detail.page.team_id,
                    "updated_at":objective_detail.page.updated_at
                },
                "messages":[
                    {
                    "_type":"message",
                    "body_preview":None,
                    "id":"d2900d8c-f45c-4727-9541-8490e2d26cc1",
                    "is_archived":False,
                    "objective_id":"4e1624ff-317e-4004-9e49-acefca78100a",
                    "team_id":"b75eae33-a047-4792-914c-94f02ae6cdec",
                    "type":"email"
                    }
                ]
            }
            payload['objective_rows'].append()

    def list(self):
        self.req = requests.get('https://api.digitalonboarding.com/v1/campaigns', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_campaigns = []
        for x in self.data:
            list_campaigns.append(campaign(x, self.Client))
        return list_campaigns