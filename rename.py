# -*- coding: utf-8 -*-

import urllib.parse
import random
import oauth2
import config


def oauth_req(
        url,
        key,
        secret,
        http_method="GET",
        post_body=b"",
        http_headers=None):
    consumer = oauth2.Consumer(
            key=config.consumer_key,
            secret=config.consumer_secret)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(
            url,
            method=http_method,
            body=post_body,
            headers=http_headers)
    return content


with open('renamelist.txt', 'r', encoding="utf-8") as f:
    renamelist = f.readlines()

while True:
    new_name = random.sample(renamelist, 1)[0]
    new_name = new_name.replace('<Name>', config.name)
    if(len(new_name) <= 20):
        break

print('Your new name is "' + new_name + '"\n')

home_timeline = oauth_req(
        'https://api.twitter.com/1.1/account/update_profile.json?name=' +
        urllib.parse.quote(new_name),
        config.access_token,
        config.access_token_secret,
        http_method="POST")
