# coding=utf-8
import requests
class Tieba:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        # “kw=”的后面是接的贴吧的名字，而“pn=”的后面是接的页数
        self.url_temp ="https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        }
    def get_url_list(self):
        # 构造url列表
        return [self.url_temp.format(i* 50) for i in range(100)]


    def parse_url(self,url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self,html_str,page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(html_str)


    def run(self):#实现主要逻辑
        # 1.构造url列表
        url_list = self.get_url_list()

        # 2.遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.保存
            page_num = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_num)


if __name__ == '__main__':

    tieba = Tieba('切尔西')
    tieba.run()
