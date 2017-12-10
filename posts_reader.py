#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os.path
import json
import pickle
import datetime
import urlparse
import pytz
import pycurl
import requests
import facebook

from make_index import make_index

def to_jst(datestring):
    date_obj = datetime.datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S+0000").replace(tzinfo=pytz.timezone('UTC'))
    return datetime.datetime.strftime(date_obj.astimezone(pytz.timezone('Japan')), "%Y-%m-%d %H:%M:%S %Z")
    
def get_file(url):
    name = 'photos/' + url.rsplit('/', 1)[1].split('?')[0]
    if name[-3:] == "php":
        url=urlparse.parse_qs(url)['url'][0]
        name = 'photos/' + url.rsplit('/', 3)[1] + '-' + url.rsplit('/', 1)[1].split('?')[0]
    if not(os.path.isfile(name)):
        with open(name, 'wb') as f:
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, url)
            curl.setopt(pycurl.TIMEOUT, 6)
            curl.setopt(pycurl.USERAGENT, "Mozila/5.0")
            curl.setopt(pycurl.WRITEFUNCTION, f.write)
            curl.perform()
    return "［＃挿絵（" + name.encode('utf-8') + "）入る］"

class PostsReader:
    TOKEN_JSON = 'token.json'

    def __init__(self):
        self.indexes={ "posts": 0, "photos": 0, "cover_photos": 0, "profile_photos": 0 }
        self.alldata={ "posts": [], "photos": [], "cover_photos": [], "profile_photos": [] }
        self.allposts = []
        user_access=""
        with open(PostsReader.TOKEN_JSON, 'r') as f:
             user_access = json.load(f)['token']['user_access']
            
        self.graph = facebook.GraphAPI(user_access['access_token'])
        
        try:
            for fname in [ "posts", "photos", "cover_photos", "profile_photos" ]:
                pkl_file = open('raw_data/' + fname + '.pkl', 'rb')
                self.alldata[fname]=pickle.load(pkl_file)
                pkl_file.close()
        except IOError:
            print("file cannot be opend.")

    def get_file_from_album(self,selector):
        photo_id = self.alldata[selector][self.indexes[selector]]['id']
        url = self.graph.get_object(photo_id + '/picture')['url']
        return get_file(url)

    def epilogue_text(self,entry):
        text = "\n"
        text += "［＃３字下げ］" + to_jst(entry['created_time']).encode('utf-8') + "\n"
        text += "［＃区切り線］\n"
        return text

    def cover_or_profile_photos(self,selector,prev_created_time,next_created_time):
        prologue_text = { "cover_photos": 'ひなビタ updated their cover photo.\n', "profile_photos": 'ひなビタ updated their profile picture.\n'}
        if self.indexes[selector] < len(self.alldata[selector]):
            data=self.alldata[selector][self.indexes[selector]]
            created_time = datetime.datetime.strptime(data['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
            if prev_created_time <= created_time and created_time < next_created_time:
                text = prologue_text[selector]
                text += self.get_file_from_album(selector)
                text += self.epilogue_text(data)
                self.allposts.append(text)
                self.indexes[selector] += 1

    def dump_text(self):
        for post in self.allposts:
            print(post)

    def runner(self):
        self.allposts.append(make_index(0))
        for entry in self.alldata["posts"]:
            idx = make_index(entry)
            if idx != None:
                self.allposts.append(make_index(entry))

            if self.indexes["posts"] == 0:
                prev_created_time = datetime.datetime(1970, 1, 1, 0, 0, 0)
            else:
                prev_created_time = datetime.datetime.strptime(self.alldata["posts"][self.indexes["posts"]-1]['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
            next_created_time = datetime.datetime.strptime(entry['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
            self.cover_or_profile_photos("cover_photos", prev_created_time, next_created_time)
            self.cover_or_profile_photos("profile_photos", prev_created_time, next_created_time)

            self.indexes["posts"] += 1

            if entry.has_key("message"):
                text = entry['message'].encode('utf-8').replace('\r\n', '\n') + '\n'
                if self.indexes['photos'] < len(self.alldata['photos']):
                    if entry['message'] == self.alldata["photos"][self.indexes["photos"]]['name']:
                        text += self.get_file_from_album("photos")
                        self.indexes['photos'] += 1
                text += self.epilogue_text(entry)
                self.allposts.append(text)

            elif entry['story'] == u'ひなビタ shared a link.':
                response = self.graph.get_object(entry['id'] + '/attachments')
                text = entry['story'].encode('utf-8') + '\n'
                if response['data'][0].has_key("url"):
                    text += "<a href=" + response['data'][0]['url'].encode('utf-8') + ">" + response['data'][0]['title'].encode('utf-8') + "</a>"
                else:
                    text += get_file(response['data'][0]['media']['image']['src'])
                text += self.epilogue_text(entry)
                self.allposts.append(text)
