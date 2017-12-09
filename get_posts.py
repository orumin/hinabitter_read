#!/usr/bin/env python

import json
import requests
import facebook

TOKEN_JSON = 'token.json'

user_access=""
with open(TOKEN_JSON, 'r') as f:
     user_access = json.load(f)['token']['user_access']
    
graph = facebook.GraphAPI(user_access['access_token'])
resp = graph.get_object('hinabitter/posts')

allposts = []

while(True):
    try:
        for entry in resp['data']:
            if entry.has_key("message"):
                allposts.append(entry['created_time'].encode('utf-8') + '\n' + entry['message'].encode('utf-8') + '\n')
        resp = requests.get(resp['paging']['next']).json()
    except KeyError:
        break

allposts.reverse()

for post in allposts:
    print(post)
