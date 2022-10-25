from do import Client
import config

autho_token_obj = Client('https://shawn.digitalonboarding.com', 'shawn@digitalonboarding.com', config.passwd)
#new_contact = autho_token_obj.contacts().create(
#            unique_id="api_user_id",
#            name_first="api",
#            name_last="user",
#            email="apiuser@email.com",
#            phone_mobile="1234567890")
   
#print(new_contact.data['id'])

#response = autho_token_obj.contacts(new_contact.data['id']).update(birthdate='1994-11-25')
#contact = autho_token_obj.contacts('8f95bd30-3a09-4183-b956-c7e98d1036c6').get()
#print(contact.name_first)
#response = autho_token_obj.contacts('8f95bd30-3a09-4183-b956-c7e98d1036c6').delete()

contacts = autho_token_obj.contacts().list()
for contact in contacts:
    print(contact.unique_id)
    #contact.update(sms_opted_in=True)
   
#print(response.data)