import requests
from requests.auth import HTTPBasicAuth
from Config import *

def make_get_request(url):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    req = requests.get(url, auth=HTTPBasicAuth(USERNAMEISE, PASSWORDISE), headers=headers, verify=False)
    response_body = req.json()['SearchResult']['resources']
    return response_body

def get_ise_identity_group():
    print(make_get_request(IDENTITYGROUP))

def all_internal_users():
   print(make_get_request(INTERALUSERS))

def user_list():
    internal_users = make_get_request(INTERALUSERS)
    for i, entry in enumerate(internal_users):
        print(entry['name'])

def search_user(user):
    print(make_get_request(USERSEARCH + str(user)))






