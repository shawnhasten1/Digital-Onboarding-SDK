from do.do import Client
import config

do_client = Client('https://shawn.digitalonboarding.com', 'shawn@digitalonboarding.com', config.passwd)

def getContact():
    contact = do_client.contacts('eefd2965-e3aa-4a53-9ab5-683c3d34c8a4').get()
    print(contact.name_first)

def createContact():
    new_contact = do_client.contacts().create(
                unique_id="API_USER_1",
                name_first="api",
                name_last="user",
                email="apiuser@email.com",
                phone_mobile="1234567890")

def updateContact():
    contact = do_client.contacts('eefd2965-e3aa-4a53-9ab5-683c3d34c8a4').update(name_first='Shawn 1')
    print(contact.name_first)

    ## OR THE FOLLOWING
    contact_two = do_client.contacts('eefd2965-e3aa-4a53-9ab5-683c3d34c8a4').get()
    contact_two.update(name_first='Shawn 2')
    # THIS WILL PROBABLY BE CLEANED UP SO THAT IT DOESN'T HAVE TO RETRIEVE THE CHANGE
    contact_two = do_client.contacts('eefd2965-e3aa-4a53-9ab5-683c3d34c8a4').get()
    print(contact_two.name_first)

def deleteContact():
    contact = do_client.contacts('eefd2965-e3aa-4a53-9ab5-683c3d34c8a4').delete()

def uploadContacts():
    contact_list = [
        {
            'unique_id':'bulk_insert_1',
            'name_first':'John',
            'name_last':'Doe',
            'email':'bulky1@email.com'
        },
        {
            'unique_id':'bulk_insert_2',
            'name_first':'Jane',
            'name_last':'Doe',
            'email':'bulky3@email.com'
        }
    ]

    do_client.contacts().bulk_upsert(contact_list)

def uploadAccounts():
    account_list = [
        {
            'account_number':'123456', 
            'contact.unique_id':'bulk_insert_2', 
            'product.code':'TEST', 
            'product.type':'checking', 
            'nickname':'API Account 69'
        },
        {
            'account_number':'1234567', 
            'contact.unique_id':'bulk_insert_1', 
            'product.code':'TEST', 
            'product.type':'checking', 
            'nickname':'API Account 421'
        }
    ]

    do_client.contacts().accounts().bulk_upsert(account_list)

createContact()