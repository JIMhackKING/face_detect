#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) free software, GPLv3

from os import path
from bottle import run, route, request, response, static_file, error
from jinja2 import Template, FileSystemLoader, Environment
# 添加环境变量
__import__("sys").path.append("..")
from scripts import detect

env = Environment(loader = FileSystemLoader("./templates"))
with open("templates/upload.html") as f:
    uploadhtml = f.read()

# 绑定404错误界面
@error(404)
def error404(error):
    return "<h1>404:"

@route("/")
def get():
    response.set_header('Content-Type','text/html; charset=utf-8')
    return uploadhtml

@route("/<filepath:path>")
def load_file(filepath):
    return static_file(filepath, "./images")

@route("/",method = "POST")
def post():
    # 加载模板
    template = env.get_template("result.html")
    # 设置headers
    response.set_header('Content-Type','text/html; charset=utf-8')
    response.set_header('Server','Super PC Server')
    
    # 获取表单提交的文件
    file1 = request.files.get("file1")
    if not file1:
        return '<div align="center"><font size="190">文件上传失败。</font></div>'
    # 判断文件类型
    name, ext = path.splitext(file1.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return '''<div align="center"><h1><font color="#CC6633">File extension not allowed.</font></h1>
                  <h1>文件类型错误（只支持 png,jpg,jpeg 格式）或者文件名含有中文</h1></div>'''
    
    # 保存文件，并判断文件是否存在
    try:
        file1.save("./images/"+file1.filename)
    except IOError:
    	image = open("./images/"+file1.filename,'rb').read()
    	result = detect_result(image)
        s = template.render(ip_address = request["REMOTE_ADDR"],
                            filename = file1.filename,
                            explain = u"已经存在，忽略上传。",
                            result = result)
    else:
    	image = open("./images/"+file1.filename,'rb').read()
    	result = detect_result(image)
        s = template.render(ip_address = request["REMOTE_ADDR"],
                            filename = file1.filename,
                            explain = u"成功上传，尺寸为：%d bytes" %len(image),
                            result = result)
    return s

def detect_result(image):
	result_list = []
	try:
		result = detect.detect(image)["result"][0]
	except:
		return [u"检测失败，请重试"]
	# 美丑评分
	result_list.append(u"美丑打分：%d （低了不能生气）" %result["beauty"])
	# 年龄
	result_list.append(u"年龄：%d （我只是猜的）" %result["age"])
	# 表情
	if result["expression_probablity"] >= 0.9:
		if result["expression"] == 0:
			result_list.append(u"表情：不笑 （不要老板着脸，多笑有好处）")
		elif result["expression"] == 1:
			result_list.append(u"表情：微笑 （笑笑更健康）")
		elif result["expression"] == 2:
			result_list.append(u"表情：大笑 （笑的好灿烂啊）")
	# 脸型
	faceshape = [i.values() for i in result["faceshape"]]
	for index, i in enumerate(faceshape[:-1]):
		if i[1] > faceshape[index+1][1]:
			face_type = i[0]
	if face_type == "square":
		result_list.append(u"脸型：国字脸")
	elif face_type == "triangle":
		result_list.append(u"脸型：瓜子脸")
	elif face_type == "oval":
		result_list.append(u"脸型：椭圆脸")
	elif face_type == "heart":
		result_list.append(u"脸型：心形脸")
	elif face_type == "round":
		result_list.append(u"脸型：圆脸")
	# 性别
	if result["gender_probability"] >= 0.99:
		if result["gender"] == "male":
			result_list.append(u"性别：男")
		else:
			result_list.append(u"性别：女")
	# 佩戴眼镜
	if result["glasses_probability"] >= 0.9:
		if result["glasses"] == 0:
			result_list.append(u"无佩戴眼镜")
		elif result["glasses"] == 1:
			result_list.append(u"佩戴普通眼镜")
		elif result["glasses"] == 2:
			result_list.append(u"佩戴墨镜")
	# 人种
	if result["race_probability"] >= 0.99:
		if result["race"] == "yellow":
			result_list.append(u"人种：黄")
		elif result["race"] == "white":
			result_list.append(u"人种：白")
		elif result["race"] == "black":
			result_list.append(u"人种：黑")
		elif result["race"] == "arabs":
			result_list.append(u"人种：阿拉伯人")

	return result_list

if __name__ == '__main__':
    run()
