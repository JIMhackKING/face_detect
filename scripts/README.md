## access_token.py

百度调用接口需要AcessToken参数，这个模块就是用来获取AcessToken的，完全自动化。
## detect.py

通过API获取人脸检测的结果，可以是本地图片也可以是网络图片
## match.py

通过API进行两张图片的人脸对比，可以是本地图片也可以是网络图片
## encrypt.py

文档、字符串的加密模块，用三层加密来加密字符串，可以加密账号或者密码等一切涉及安全问题的内容。

加密步骤：<br/>
1. 字符替换<br/>
2. ASCII码转换<br/>
3. base64编码<br/>