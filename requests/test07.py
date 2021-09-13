import requests

url = 'https://github.com/ZackOnez'

# 构造请求头字典
headers = {
    # 从浏览器中复制过来的User-Agent
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    # 从浏览器中复制过来的cookie
    'Cookie': '_device_id=d66ebc4fcab52942e2b8a933af051f0e; _octo=GH1.1.452302126.1631513466; tz=Asia%2FShanghai; has_recent_activity=1; user_session=OFGn2djgpax9ckkdoJLr2xErTfim-xufxdrO9GDSlodBmlhI; __Host-user_session_same_site=OFGn2djgpax9ckkdoJLr2xErTfim-xufxdrO9GDSlodBmlhI; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=ZackOnez; _gh_sess=lfnAc0m9iAa4Qu1EOXOMFGJ7%2FfmTD703gv%2FNVFu4bV8frmg%2FbE%2BxAFuSwJGEjVpGJKpedAqM0QTdaYcHJ%2FTG4vYCk8byZN3IakyQqZ7HIHioOZJcIsVe8rj5i10u02Wa4LVZTOAqx5yzfPrZGuAn%2FPzIVGkIRRufk2qLXzGHQGQ3IW93gIwzNbQKUUJguZ4fNmbeK0n%2BWhM%2BtveFMd5FSUMszL0oJmP0Nf5ejAxmkb9FGbGfF3dO91kdgDVI4dt7YedfyIkF8ZYF56f4m25BZY4PMymmDe1rGEfdZn9ErBQvgcspObCEkM%2F0EkdHCuBmvKO%2BrEXkEDCT6XExL8zaFXTiFNPEau8jQMK3AbBnI6LT0DjXa5%2FED0f%2BUCsJNv8XpEIbbG61BIoDXIDx8S7w4m8t54rz%2FOlAb%2BTKcQOxFv5ppwDkQGZirjYb9OarDlyW10QfJtUbPMpCYtCmCUDCQzRBCMnkrymSHvzrLMh6dSE0%2FuVz95sk%2F%2Fjn5xC4iTMeLfdugX670mfP%2BW9S6z3k6YpUz7ZKCitREGMmTE%2BnikDAn9L4bzt2YvjYH2liXxcAzyJmQ1QLGFR3xzorIYhlC3up31R%2Fp5njlyPtew64HtV7OHwF%2FQ2hz3Eq96kV9lfOepd%2Bdx0wk0Zl3x1sGe%2FG4ii4vKPowTBQrFVh1osl7SmEuDOUcrpDOxoGzwt%2BviJkvD0f%2BWNjMtb5EL737n674B%2Bvd4dgYGqGpcT6KQxse7FuvyH90dgUVYrDGjguLbF1rU1t1Ol2l8Vv%2FgRiJcy2g8BkIOz5n0kdTq3RPhPeuglakUfciexG1nE%2B4dA18HD4Mzx3mX511nHWrMWlZDHoJcWeUJ8WpKq6rvwXuFmBEEOuAWmveT9lVWMSBc72yH6ChCVRxqRASdzbFTOZPXNZMfgVVNWEKpb1d7DDRDNo9KQwPIBd9yWfuxL7nrt31mgH%2BKO5HCX1xlPJaqyD--JvG%2FMi6kYzW71toJ--uwh5x%2BU%2FU%2Fe4hJtIuh8qpA%3D%3D'
}

# 请求头参数字典中携带cookie字符串
response = requests.get(url, headers=headers)

print(response.text)
