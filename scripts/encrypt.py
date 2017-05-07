# coding:utf-8
"""这个程序用于进行字符串混淆加密，完美支持英文和中文。
可以加密所有字符串，例如账号、密码或者是一些敏感的词汇，甚至是一个文件。
最重要的是可以多次加密同一段字符，加密加密后的内容。
此版本为 Python3 ，base64 需要用 bytes 类型，如果是 Python2 不需要编码和解码.
这个程序同样也可以加密一个文件"""
__author__ = "JIMhackKING"

# this 的 d 很好的做了代码混淆的字典，可是在导入时会打印一段内容
# from this import d
import base64
import json

d = {'A': 'N', 'C': 'P', 'B': 'O', 'E': 'R', 'D': 'Q', 'G': 'T', 'F': 'S', 'I': 'V',
 'H': 'U', 'K': 'X', 'J': 'W', 'M': 'Z', 'L': 'Y', 'O': 'B', 'N': 'A', 'Q': 'D',
 'P': 'C', 'S': 'F', 'R': 'E', 'U': 'H', 'T': 'G', 'W': 'J', 'V': 'I', 'Y': 'L',
 'X': 'K', 'Z': 'M', 'a': 'n', 'c': 'p', 'b': 'o', 'e': 'r', 'd': 'q', 'g': 't',
 'f': 's', 'i': 'v', 'h': 'u', 'k': 'x', 'j': 'w', 'm': 'z', 'l': 'y', 'o': 'b',
 'n': 'a', 'q': 'd', 'p': 'c', 's': 'f', 'r': 'e', 'u': 'h', 't': 'g', 'w': 'j',
 'v': 'i', 'y': 'l', 'x': 'k', 'z': 'm'}

# 给定一个字符串，对该字符串进行混淆和加密，防止明文密码出现在源码或程序输出中
def str_encode(string):
	# 创建第一个新的空字符变量，储存第一次混淆后的字符串（字符替换）
	new_string1 = ""
	for i in string:
		try:
			new_string1 += d[i]
		except:
			new_string1 += i

	# 创建第二个新的空字符变量，储存第二次混淆后的字符串（ASCII码转换）
	new_string2 = ""
	for i in new_string1:
		new_string2 += str(ord(i)) + ",~!"

	# 创建第三个新的空字符变量，储存第三次混淆后的字符串（base64加密）
	last_string = base64.b64encode(new_string2)
	return last_string

def str_decode(string):
	# 创建第一个变量储存 base64 解码后的内容
	new_string1 = base64.b64decode(string)
	# 创建第二个变量储存 ASCII 码转换后的内容
	new_string2 = ''.join([chr(int(i)) for i in new_string1.split(",~!")[:-1]])

	# 创建第三个变量春粗字符替换后的最终结果
	last_string = ""
	for i in new_string2:
		try:
			last_string += d[i]
		except:
			last_string += i

	return last_string

if __name__ == '__main__':
	API_key = ""
	Secret_key = "我"
	
	# 为了保密，这里不给出明文的 API Key 和 Secret Key
	s1 = str_encode(API_key)
	print str_decode(s1)
	s2 = str_encode(Secret_key)
	print str_decode(s2)
