import requests
import json

class King(object):

    def __init__(self, word):
        self.url = "http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=b0a0e4a1f9630d89"
        self.word = word
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
        self.post_data = {
            "from": "zh",
            "to": "en",
            "q": "人生苦短,我用python"
        }

    def get_data(self):
        response = requests.post(self.url, headers=self.headers, data=self.post_data)
        # 默认返回bytes类型，除非确定外部调用使用str才进行解码操作
        return response.content

    def parse_data(self, data):

        # 将json数据转换成python字典
        dict_data = json.loads(data)

        # 从字典中抽取翻译结果
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])

    def run(self):
        # url
        # headers
        # post--data
        # 发送请求
        data = self.get_data()
        # 解析
        self.parse_data(data)


if __name__ == '__main__':
    king = King("人生苦短，我用python")
    king.run()
