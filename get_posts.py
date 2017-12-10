#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import os.path
import json
import pickle
import requests
import facebook

TOKEN_JSON = 'token.json'

def paging(fname):
    data=[]
    full_fname='raw_data/'+ fname +'.pkl'
    if os.path.isfile(full_fname):
        with open(full_fname, 'rb') as pkl_file:
            data=pickle.load(pkl_file)
    resp={}
    if fname == "posts":
        resp = graph.get_object('hinabitter/posts')
    else:
        resp = graph.get_object(album_id[fname] + '/photos')
    new_data=[]
    while(True):
        try:
            for entry in resp['data']:
                if not data:
                    new_data.append(entry)
                elif data[0]['id'] == entry['id']:
                    raise KeyError('updated')
                else:
                    new_data.append(entry)
            resp=requests.get(resp['paging']['next']).json()
        except KeyError:
            break
    if not new_data:
        return
    elif data:
        new_data.extend(data)
    with open(full_fname, 'wb') as f:
        pickle.dump(new_data,f)

user_access=""
with open(TOKEN_JSON, 'r') as f:
     user_access = json.load(f)['token']['user_access']
    
graph = facebook.GraphAPI(user_access['access_token'])

albums = graph.get_object('hinabitter/albums')
album_id = { "photos": "", "cover_photos": "", "profile_photos": "" }
for entry in albums['data']:
    if entry['name'] == "Timeline Photos":
        album_id["photos"] = entry['id']
    elif entry['name'] == "Cover Photos":
        album_id['cover_photos'] = entry['id']
    elif entry['name'] == "Profile Pictures":
        album_id['profile_photos'] = entry['id']

for fname in ["posts", "photos", "cover_photos", "profile_photos"]:
    paging(fname)
