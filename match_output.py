# coding:utf-8
"""
作者 ：JIMhackKING
"""

from scripts import match

# 打开图片必须用 rb 格式打开，否则会返回图片格式错误
with open(r"image\21906d7d07145d9c-131ab1edf2604fc1-596790b861cf682d4e3dafb6f0d0d44b.jpg",'rb') as f:
	image1 = f.read()
with open(r"image\d7036c9a17f5fda2-d9a61ab1a5c30897-5b7b84377a495114073c7cfa5a654782.jpg",'rb') as f:
	image2 = f.read()

try:
	result = match.match(image1, image2)["result"][0]["score"]
except:
	print u"比对失败，请重试"
	exit()
	
# 比对结果
print u"比对结果：%d 分" %result