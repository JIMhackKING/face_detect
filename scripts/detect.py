# encoding:utf-8
"""人脸检测模块"""
__author__ = "JIMhackKING"

import base64
import requests
import json
import access_token

'''
人脸检测接口
'''
# 传入的参数为图片的内容，不能是 bytes
def detect(image):
	img = base64.b64encode(image)

	detectUrl = "https://aip.baidubce.com/rest/2.0/face/v1/detect"
	# 参数image：图像base64编码，max_face_num：最多处理人脸数目，默认值1，face_fields：包括age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities信息，逗号分隔，默认只返回人脸框、概率和旋转角度
	params = {"max_face_num": 1, "face_fields": "age,beauty,expression,faceshape,gender,glasses,race",
	          "image": img}

	token = access_token.AuthService()
	detectUrl = detectUrl + "?access_token=" + token
	request = requests.post(detectUrl, data=params, headers = {'Content-Type':'application/x-www-form-urlencoded'})

	content = request.content
	if content:
	    return json.loads(content)
