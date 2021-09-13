import requests

# 目标url
url = 'https://www.baidu.com'

# 向目标url发送get请求
response = requests.get(url)

# 打印响应url
print(response.url)
# 打印响应的状态码
print(response.status_code)
# 打印响应对象的请求头
print(response.request.headers)
# 打印响应头
print(response.headers)
# 打印请求携带的cookies
print(response.request._cookies)
# 打印响应中携带的cookies
print(response.cookies)
