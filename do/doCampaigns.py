import requests

class campaign:
    def __init__(self, data, Client):
        self.Client = Client
        self.data = data

        self.analytics = data['analytics']
        self.custom_css = data['custom_css']
        try:
            self.template_pages = data['template_pages']
        except:
            self.template_pages = None
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
    def __init__(self, Client, campaign_id = None):
        self.Client = Client
        self.req = None
        self.status_code = None
        self.data = None

        self.campaign_id = campaign_id
        self.name = None

        self.doJourneys = None

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
                "id":objective_detail.id,
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
                "messages":[]
            }
            payload['objective_rows'].append(objective)

    def list(self):
        self.req = requests.get('https://api.digitalonboarding.com/v1/templates?include_archived=false&sort_column=inserted_at&sort_direction=desc&with_facts=true', headers=self.Client.default_headers)

        self.status_code = self.req.status_code
        self.data = self.req.json()
        list_campaigns = []
        for x in self.data:
            list_campaigns.append(campaign(x, self.Client))
        return list_campaigns

    def journeys(self, journey_id = None):
        if self.doJourneys == None:
            from do.doJourneys import journeys
            self.doJourneys = journeys(self.Client, self.campaign_id, journey_id)
        if journey_id:
            self.doJourneys.journey_id = journey_id
        return self.doJourneys

    def analytics(self, limit=20, offset=0, sort_col='timestamp', sort_dir='desc', start_date=None, end_date=None, filters=[]):
        """LIST OF FILTERS AVAILABLE
        auth_code_sent
        auth_failed
        auth_presented
        auth_succeeded
        card_on_file_abandoned
        card_on_file_completed
        card_on_file_failed
        contact_method_verified
        cta_clicked
        direct_deposit_completed
        direct_deposit_company_searched
        direct_deposit_failed
        direct_deposit_followup_cta_clicked
        direct_deposit_payroll_searched
        direct_deposit_started
        direct_deposit_widget_opened
        email_opened
        enrollment_accepted
        enrollment_declined
        enrollment_started
        enrollment_terms_link_clicked
        journey_completed
        journey_opened
        message_bounced
        message_failed
        message_sent
        message_skipped
        mobile_app_download_link_clicked
        mobile_app_download_sms_sent
        objective_completed
        opted_in
        opted_out
        page_completed
        page_confirmed
        page_viewed
        sms_received
        survey_completed
        survey_question_answered
        token_errored
        """
        url = f'https://api.digitalonboarding.com/v1/templates/{self.campaign_id}/actions?&limit={limit}&offset={offset}&sort_column={sort_col}&sort_direction={sort_dir}'
        for filter in filters:
            url += f'&name[]={filter}'
        if start_date:
            url += f'&start_date={start_date}'
        if end_date:
            url += f'&end_date={end_date}'
        self.req = requests.get(url, headers=self.Client.default_headers)
        return self.req.json()

    def page_stats(self, start_date=None, end_date=None):
        url = f'https://api.digitalonboarding.com/v1/templates/{self.campaign_id}/insights/page-stats?blank=blank'
        if start_date:
            url += f'&start_date={start_date}'
        else:
            url += f'start_date'
        if end_date:
            url += f'&end_date={end_date}'
        else:
            url += f'&end_date'
        self.req = requests.get(url, headers=self.Client.default_headers)
        try:
            return self.req.json()['value']['page_details']
        except:
            return []

    def message_performance(self, start_date=None, end_date=None):
        url = f'https://api.digitalonboarding.com/v1/templates/{self.campaign_id}/insights/message-performance?'
        if start_date:
            url += f'&start_date={start_date}'
        else:
            url += f'&start_date'
        if end_date:
            url += f'&end_date={end_date}'
        else:
            url += f'&end_date'
        self.req = requests.get(url, headers=self.Client.default_headers)
        rows = []
        for row in self.req.json()['rows']:
            rows.append({
                "bounce_rate":row['bounce_rate'],
                "click_thru_rate":row['click_thru_rate'],
                "cta_clicked":row['cta_clicked'],
                "email_click_to_open_rate":row['email_click_to_open_rate'],
                "email_open_rate":row['email_open_rate'],
                "email_opened":row['email_opened'],
                "id":row['id'],
                "message_bounced":row['message_bounced'],
                "message_sent":row['message_sent'],
                "opted_out":row['opted_out'],
                "unsubscribe_rate":row['unsubscribe_rate']
            })
        return rows

    def objective_performance(self, start_date=None, end_date=None):
        url = f'https://api.digitalonboarding.com/v1/templates/{self.campaign_id}/insights/objective-performance?blank=blank'
        if start_date:
            url += f'&start_date={start_date}'
        else:
            url += f'&start_date'
        if end_date:
            url += f'&end_date={end_date}'
        else:
            url += f'&end_date'
        self.req = requests.get(url, headers=self.Client.default_headers)
        try:
            return self.req.json()['value']['result']
        except:
            return []