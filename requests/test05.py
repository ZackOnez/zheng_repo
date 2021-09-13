import requests

# 构建请求头字典
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}

url = 'https://www.baidu.com/s?wd=python'

# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)
