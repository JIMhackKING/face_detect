# encoding:utf-8
"""获取 Acess Token """
__author__ = "JIMhackKING"

import urllib
import urllib2
import json
import encrypt
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
filePath = ROOT + "/auth.json"

with open(filePath) as f:
    auth_key = json.load(f)

def AuthService():
    # 获取token地址
    authHost = "https://aip.baidubce.com/oauth/2.0/token?"
    # 官网获取的 API Key
    clientId = encrypt.str_decode(auth_key["API_key"])
    # 官网获取的 Secret Key
    clientSecret = encrypt.str_decode(auth_key["Secret_key"])
    getAccessTokenUrl = authHost + "grant_type=client_credentials" + "&client_id=" + clientId + "&client_secret=" + clientSecret
    request = urllib2.Request(getAccessTokenUrl)
    response_data = urllib2.urlopen(request)
    params = json.loads(response_data.read())

    auth_key["acess_token"] = encrypt.str_encode(params["access_token"])
    with open(filePath,'w') as f:
        json.dump(auth_key, f, indent = 2, sort_keys = True)

    return params["access_token"]

if __name__ == '__main__':
    print AuthService()