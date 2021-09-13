import requests

url = 'https://github.com/ZackOnez'

# 构造请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
}

# 构造cookies字典
cookies_str = '_device_id=d66ebc4fcab52942e2b8a933af051f0e; _octo=GH1.1.452302126.1631513466; tz=Asia%2FShanghai; has_recent_activity=1; user_session=OFGn2djgpax9ckkdoJLr2xErTfim-xufxdrO9GDSlodBmlhI; __Host-user_session_same_site=OFGn2djgpax9ckkdoJLr2xErTfim-xufxdrO9GDSlodBmlhI; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=ZackOnez; _gh_sess=8Hdtpxb7As0wW4kyHaet8O69XMAMt7L4yeAhCwniWr7OPz%2B2TiBg9fleb%2B0am40Pa%2BTvuyTYYC%2BfE55IbZrr9Fk%2Flnzj9LOkNC5QE4kEW9hLEfmLv64u7QRrlfv9%2F821wbFlkfeV%2B9To%2BL4A5%2BSf2LPtUVIm1qdFYUv2TS77yKTPSVd3OLd7IvfNG%2BwSm%2BnksJs%2BSCL2avt4uECcurq2I62QFTXoMmzDo0XgUqtwY2kaQ19SccjKowUj%2BsZ5I3d%2B0zqzYmioSzCaFCCPt7yowmHp8yVOQQyJM7C6Yp%2F2fMumf%2F686lrX50I8B8%2FLg84eSSMxh%2FKDbPzbeYKlaOgkNVxDycV%2Br1sQoQm9ek4%2FcWXhsok550HEEfGQ21USQSadhPHtC%2F0bR1c4hY7LfwMXrC9nq83j0XCKcy%2FCVo1JmhkVww4v1KZUJEB%2FMr6A1PF9zOaNJDPI4IO2XUU9TOO6rGW9GL36QGHx0andLssjQvsGrN2CUOOCk1TrJZ83g4yQHk73z7XlxlEBlq0HUTCrcZZg%2Bzy1ZPtadmw%2BcgnDB%2FkB3UrlFO8QdmnjaNAc5se6qYdsVQ8qJPDqXWBUh3hJLpOzt0xji0xZ%2BkRCCcEnJs1sRi4RqssPbOQOu5Hstje%2F6J86zcvnizPqpiShysNaxiV16uAPVOVZb9MJotKivZiqFjf1xzkgx4qlfYrmlLs0MTcIWNl3SJcz%2BBCvy1WDd6YAGUGWp890dF23MW4Td78MEgNsp%2FY4vyoYuM3CGT8B--ypv%2F8MwoU2FkC8Wj--16zd3Z4QhtcF4%2FS3Duz6Ng%3D%3D'
cookies_dict = {cookie.split('=')[0]:cookie.split('=')[-1] for cookie in cookies_str.split('; ')}

# 请求擦拭农户字典中携带cookie字符串
response = requests.get(url, headers=headers, cookies=cookies_dict)

print(response.text)
