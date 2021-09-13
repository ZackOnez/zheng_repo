# 导入requests模块
import requests

# 目标url
url = 'http://www.baidu.com'

# 向目标url发送get请求
response = requests.get(url)

# 打印响应内容
# 方式一
# response.encoding = 'utf8'
# print(response.text)
# 方式二
print(response.content.decode())  # 注意这里
