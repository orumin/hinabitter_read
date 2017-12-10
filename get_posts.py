#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import pickle
import requests
import facebook

TOKEN_JSON = 'token.json'

def paging(data_array,data):
    while(True):
        try:
            for entry in data_array['data']:
                data.append(entry)
            data_array=requests.get(data_array['paging']['next']).json()
        except KeyError:
            break
    data.reverse()

user_access=""
with open(TOKEN_JSON, 'r') as f:
     user_access = json.load(f)['token']['user_access']
    
graph = facebook.GraphAPI(user_access['access_token'])

with open('raw_data/posts.pkl', 'wb') as f:
    posts = graph.get_object('hinabitter/posts')
    posts_data=[]
    paging(posts,posts_data)
    pickle.dump(posts_data,f)

albums = graph.get_object('hinabitter/albums')
album_timeline_id=""
album_cover_id=""
album_profile_id=""
for entry in albums['data']:
    if entry['name'] == "Timeline Photos":
        album_timeline_id = entry['id']
    elif entry['name'] == "Cover Photos":
        album_cover_id = entry['id']
    elif entry['name'] == "Profile Pictures":
        album_profile_id = entry['id']

with open('raw_data/photos.pkl', 'wb') as f:
    photos = graph.get_object(album_timeline_id + '/photos')
    photos_data=[]
    paging(photos,photos_data)
    pickle.dump(photos_data,f)

with open('raw_data/cover_photos.pkl', 'wb') as f:
    cover_photos = graph.get_object(album_cover_id + '/photos')
    cover_photos_data=[]
    paging(cover_photos,cover_photos_data)
    pickle.dump(cover_photos_data,f)

with open('raw_data/profile_photos.pkl', 'wb') as f:
    profile_photos = graph.get_object(album_profile_id + '/photos')
    profile_photos_data=[]
    paging(profile_photos,profile_photos_data)
    pickle.dump(profile_photos_data,f)
