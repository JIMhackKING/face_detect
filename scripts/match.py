# encoding:utf-8
"""人脸比对模块"""
__author__ = "JIMhackKING"

import base64
import requests
import json
import access_token

'''
人脸比对接口
'''
def match(image1, image2):
	img1 = base64.b64encode(image1)
	img2 = base64.b64encode(image2)

	matchUrl = "https://aip.baidubce.com/rest/2.0/face/v2/match"
	# 参数images：图像base64编码,多张图片半角逗号分隔
	params = {
	    "images": "%s,%s" %(img1,img2)}

	token = access_token.AuthService()
	matchUrl = matchUrl + "?access_token=" + token
	req = requests.post(matchUrl, params, headers = {'Content-Type': 'application/x-www-form-urlencoded'})

	content = req.content
	if content:
	    return json.loads(content)