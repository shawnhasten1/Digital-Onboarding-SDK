from do.do import Client
import config

do_client = Client('https://shawn.digitalonboarding.com', 'shawn@digitalonboarding.com', config.passwd)

found_journeys = True
while found_journeys:
    journeys = do_client.campaigns('c0b56af5-7363-44b8-b09e-136451e6b50e').journeys().list()
    if journeys:
        for journey in journeys:
            journey.delete()
    else:
        found_journeys = False