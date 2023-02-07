/*PyMACS, Design Document 001

Design of PyMACS
1. Thread-based, browser OS with a unified browser-based thread map.
2. Inter Thread communication by resident RAM disk.
3. Symmetric Threads.
4. Applets, and repls in browser
5. python based.
6. pymacs kernel
7. XML=JSON=DOM
8. All storage is in JSON
9. coding in XML and DOM, all content, code, and data are in DOM, on the browser.

How pymacs goes beyond FreeRTOS for IoT
How Pymacs is different from pickle import EXT4
from platform import python_branch
from subprocess import CREATE_NEW_CONSOLE
from types import MemberDescriptorType
from circuit python and micropython.*/

%pymacs functions and APIs
%python
%US001: define a function to parse URLs
def parse_url(url):
    import urllib.parse
    return urllib.parse.urlparse(url)

%python
%US002: define a function to call google API on query string and return JSON
def google_api(query):
    import urllib.request
    import json
    url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY&cx=017576662512468239146:omuauf_lfve&q=' + query
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data

%python
%US003: define function to query JSON data for images and print all images to console
def print_images(data):
    import json
    import urllib.request
    import urllib.parse
    import urllib.error
    import re
    for item in data['items']:
        url = item['link']
        title = item['title']
        img = item['image']['thumbnailLink']
        print(url)
        print(title)
        print(img)
        print('\n')

%python
%US004: define function to query JSON data for videos and print all videos to console
def print_videos(data):
    import json
    import urllib.request
    import urllib.parse
    import urllib.error
    import re
    for item in data['items']:
        url = item['link']
        title = item['title']
        img = item['image']['thumbnailLink']
        print(url)
        print(title)
        print(img)
        print('\n')

%python
%US005: define function to query JSON data for news and print all news to console
def print_news(data):
    import json
    import urllib.request
    import urllib.parse
    import urllib.error
    import re
    for item in data['items']:
        url = item['link']
        title = item['title']
        img = item['image']['thumbnailLink']
        print(url)
        print(title)
        print(img)
        print('\n')

%python
%US006: define function to query JSON data for maps and print all maps to console
def print_maps(data):
    import json
    import urllib.request
    import urllib.parse
    import urllib.error
    import re
    for item in data['items']:
        url = item['link']
        title = item['title']
        img = item['image']['thumbnailLink']
        print(url)
        print(title)
        print(img)
        print('\n')

%python
%US007: define function  to query JSON data with query string and pass results to BERT summarization API, print result to console
def summarize(data):
    import json
    import urllib.request
    import urllib.parse
    import urllib.error
    import re
    import requests
    url = 'http://bert.cs.columbia.edu/summarize?text=' + data
    response = requests.get(url)
    data = json.loads(response.text)
    return data


%python
%US009: define function to use twillio api to call number and send message
def call_number(number, message):
    import twilio
    from twilio.rest import Client
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=number,
        from_='+141599261222',
        body=message)
    return message

%python
%US010: define function to use twillio api to recieve a meaage from number n and summarize results with function summarize
def recieve_message(number):
    import twilio
    from twilio.rest import Client
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=number,
        from_='+141599261222',
        body='Hello there!')
    return summarize(message)

%python
%US011: define function to use twillioML file twilliomlfile to create a autoresponse agent for number n 
def create_agent(number, twilliomlfile):
    import twilio
    from twilio.rest import Client
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    agent = client.taskrouter.workspaces.create_task_queue_agent(
        workspace_sid='WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        friendly_name='Agent',
        reservation_activity_sid='WAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        target_workers='lambda_worker',
        task_routing_policy='round_robin')
    return agent



%python   
%US012: define function to print JSON to CREATE_NEW_CONSOLE
def print_json(data):
    import json
    print(json.dumps(data, indent=4, sort_keys=True))

%python
%US013: transpile JSON to DOM for browser
def json_to_dom(data):
    import json
    import xml.dom.minidom
    return xml.dom.minidom.parseString(json.dumps(data, indent=4, sort_keys=True))

%python
%US013: transpile JSON to XML for browser
def json_to_xml(data):
    import json
    import xml.etree.ElementTree as ET
    return ET.fromstring(json.dumps(data, indent=4, sort_keys=True))    

%python
%US015: print DOM to console as HTML
def print_dom(dom):
    import xml.dom.minidom
    print(xml.dom.minidom.parseString(dom.toprettyxml()).toprettyxml())

%python
%USB017: create EXT4 ram file system in Memory
def create_ram_fs(size):
    import os
    import subprocess
    subprocess.call(['mkfs.ext4', '-F', '-b', '4096', '-L', 'ramfs', '-m', '0', '-d', '0', '-i', '0', '-I', '0', '-O', '^has_journal', '-O', '^has_ordered_ancestors', '-O', '^has_unordered_ancestors', '-O', '^has_sparse_super', '-O', '^has_large_file', '-O', '^has_huge_file', '-O', '^has_projected_inodes', '-O', '^has_projected_extents', '-O', '^has_uninit_inode_table', '-O', '^has_uninit_extents', '-O', '^has_uninit_block_bitmap', '-O', '^has_uninit_inode_bitmap', '-O', '^has_uninit_inode_table', '-O', '^has_uninit_extents', '-O', '^has_uninit_block_bitmap', '-O', '^has_uninit_inode_bitmap', '-O', '^has_uninit_inode_table', '-O', '^has_uninit_extents', '-O', '^has_uninit_block_bitmap', '-O', '^has_uninit_inode_bitmap', '-O', '^has_uninit_inode_table', '-O', '^has_uninit_extents', '-O', '^has_uninit_block_bitmap', '-O', '^has_uninit_inode_bitmap', '-O', '^has_uninit_inode_table', '-O', '^has_uninit_extents', '-O', '^has_uninit_block_bitmap', '-O', '^has_uninit_inode_bitmap', '-O', '^
    
%python
%US019: print memory from address a to address b to console
def print_memory(a, b):
    
