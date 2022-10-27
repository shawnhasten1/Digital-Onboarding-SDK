from do.do import Client
import config

do_client = Client('https://shawn.digitalonboarding.com', 'shawn@digitalonboarding.com', config.passwd)

objectives = do_client.objectives().list()
for objective in objectives:
    do_client.contacts('528549e3-b422-4db1-9de2-be2347664b50').updateObjective(objective.id, 'complete')