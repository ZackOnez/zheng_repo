import requests

url = 'https://www.baidu.com'

response = requests.get(url)

print(response.content.decode())

# 打印响应对象请求的请求头信息
print(response.request.headers)
