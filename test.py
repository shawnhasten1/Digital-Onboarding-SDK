from do.do import Client
import config

do_client = Client('https://mobiloilcu.digitalonboarding.com/', 'shawn@digitalonboarding.com', config.passwd)
#new_contact = do_client.contacts().create(
#            unique_id="api_user_id",
#            name_first="api",
#            name_last="user",
#            email="apiuser@email.com",
#            phone_mobile="1234567890")
#
#print(new_contact.data['id'])
#
#response = do_client.contacts(new_contact.data['id']).update(birthdate='1994-11-25')
#contact = do_client.contacts('8f95bd30-3a09-4183-b956-c7e98d1036c6').get()
#print(contact.name_first)
#response = do_client.contacts('8f95bd30-3a09-4183-b956-c7e98d1036c6').delete()
#
#contacts = do_client.contacts().list()
#for contact in contacts:
#    print(contact.unique_id)
#    #contact.update(sms_opted_in=True)
#
#print(response.data)
#
#print('OBJECTIVES\n')
#
#objectives = do_client.objectives().list()
#for objective in objectives:
#    print(objective.id)
#
#print('\nPAGES\n')
#
#objective_pages = do_client.pages().list()
#for page in objective_pages:
#    print(page.content_name)
#
#print('\nOBJECTIVE PAGES\n')
#
#objective_pages = do_client.objectives('c96da55d-8885-4ff2-aa79-710df9d67ba5').pages().list()
#for page in objective_pages:
#    print(page.content_name)
#
#print('\nOBJECTIVE MESSAGES\n')
#
#objective_messages = do_client.objectives('c96da55d-8885-4ff2-aa79-710df9d67ba5').messages().list()
#for message in objective_messages:
#    print(f'{message.type} - {message.content_name}')
#
#messages = do_client.messages().list()
#for message in messages:
#    print(f'{message.type} - {message.content_name}')
#
#campaigns = do_client.campaigns().list()
#for campaign in campaigns:
#    print(f'{campaign.name}')
#
#journeys = do_client.campaigns('cae62804-149d-4821-9027-a4e0911ca190').journeys().list()
#for journey in journeys:
#    print(f'{journey.id}')
#
#journey = do_client.journeys('8916ef47-d10a-4e4e-8c81-48f2ec878024').get()
#
#journey_2 = do_client.campaigns('af640243-b303-48ec-bd90-4fb70f023698').journeys('8916ef47-d10a-4e4e-8c81-48f2ec878024').get()
#
#do_client.journeys('8916ef47-d10a-4e4e-8c81-48f2ec878024').delete()
#
#do_client.campaigns('af640243-b303-48ec-bd90-4fb70f023698').journeys('8916ef47-d10a-4e4e-8c81-48f2ec878024').delete()
#
#journey_analytics = do_client.journeys('cab739dd-e702-4540-a1fd-c4a21a364685').analytics()
#print(journey_analytics)
#
#journey_contact = do_client.journeys('cab739dd-e702-4540-a1fd-c4a21a364685').contact().update(name_first='John')
#
#campaign_obj = do_client.campaigns('9c98efe6-d4fd-4086-b3ec-611d257ffa79')
#journey_contact = campaign_obj.journeys().create(unique_id='shawn_test_4', contact_details={'name_first':'shawn', 'name_last':'fakey', 'phone_mobile':'2392208726', 'phone_home':'2392208729'})
#try:
#    print(journey_contact.web_client_url)
#except:
#    pass

campaign_obj = do_client.campaigns('aa646b1e-d771-46c2-a752-5b31b5e24a0d')
#print(campaign_obj.analytics(filters=['email_opened']))
#print(campaign_obj.page_stats(start_date='2021-10-17', end_date='2022-10-24'))
#print(campaign_obj.message_performance(start_date='2022-10-17', end_date='2022-10-24'))
print(campaign_obj.objective_performance(start_date='2022-10-17', end_date='2022-10-24'))