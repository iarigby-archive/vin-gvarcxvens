#!/usr/bin/env python

import os
import sys
from flask import render_template
import json

def read_data(filename):
    with open(filename) as infile:
        return json.load(infile)

def read_info(base):
    return read_data(f'{base}/info.json')

class listing:
    def __init__(self, url, text, author):
        self.image_url = url
        self.text = text
        self.author = author

class person:
    def __init__(self, json_object):
        self.name = json_object['name']
        self.occupation = json_object['occupation']
        self.types = json_object['types']

def get_list():
    li = []
    base = 'static/list'
    people = os.listdir(base)
    for person_name in people:
        path = f'{base}/{person_name}'
        p_info = person(read_info(path))
        quote = os.listdir(path)
        for _, d, _ in os.walk(path):
            for quote in d:
                q_path = f'{path}/{quote}'
                q_info = read_info(q_path)
                li.append(listing(
                    url = f'{q_path}/image.jpg',
                    text = q_info['text'],
                    author = p_info
                ))
    return li

def get_main_page():
 return render_template('index.html', name='ia',
                        quotes=get_list())
