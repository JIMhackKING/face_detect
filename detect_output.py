# coding:utf-8
"""
作者 ：JIMhackKING
"""

from scripts import detect

# 打开图片必须用 rb 格式打开，否则会返回图片格式错误
with open(r"C:\Users\Administrator\Desktop\nice_20170507180549.jpg",'rb') as f:
	image = f.read()
	
try:
	result = detect.detect(image)["result"][0]
except:
	print u"检测失败，请重试"
	exit()
	
# 美丑评分
print u"美丑打分：%d （低了不能生气）" %result["beauty"]
# 年龄
print u"年龄：%d （我只是猜的）" %result["age"]
# 表情
if result["expression_probablity"] >= 0.9:
	if result["expression"] == 0:
		print u"表情：不笑 （不要老板着脸，多笑有好处）"
	elif result["expression"] == 1:
		print u"表情：微笑 （笑笑更健康）"
	elif result["expression"] == 2:
		print u"表情：大笑 （笑的好灿烂啊）"
# 脸型
faceshape = [i.values() for i in result["faceshape"]]
for index, i in enumerate(faceshape[:-1]):
	if i[1] > faceshape[index+1][1]:
		face_type = i[0]
if face_type == "square":
	print u"脸型：国字脸"
elif face_type == "triangle":
	print u"脸型：瓜子脸"
elif face_type == "oval":
	print u"脸型：椭圆脸"
elif face_type == "heart":
	print u"脸型：心形脸"
elif face_type == "round":
	print u"脸型：圆脸"
# 性别
if result["gender_probability"] >= 0.99:
	if result["gender"] == "male":
		print u"性别：男"
	else:
		print u"性别：女"
# 佩戴眼镜
if result["glasses_probability"] >= 0.9:
	if result["glasses"] == 0:
		print u"无佩戴眼镜"
	elif result["glasses"] == 1:
		print u"佩戴普通眼镜"
	elif result["glasses"] == 2:
		print u"佩戴墨镜"
# 人种
if result["race_probability"] >= 0.99:
	if result["race"] == "yellow":
		print u"人种：黄"
	elif result["race"] == "white":
		print u"人种：白"
	elif result["race"] == "black":
		print u"人种：黑"
	elif result["race"] == "arabs":
		print u"人种：阿拉伯人"
