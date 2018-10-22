import requests
from lxml import etree
from requests.exceptions import RequestException
from lxml.etree import ParseError
from jieba import analyse
tifidf = analyse.extract_tags
import json
from content_catch.content_key_catch import *

class HtmlContent(object):

    def info(self):
        #显示获取的数据信息
        print("返回数据：")
        print()


    '''
    输入url， 获取html内容
    '''
    def html_content(self , url):
        user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
        #定义用户信息
        headers = {
            'User-Agent': user_agent
        }
        #定义头部
        try:
            response = requests.get(url, headers= headers)
            response.encoding = 'utf-8'
            # 获取信息
            body = response.text
            #获取html的字符数据
        except RequestException as e:
            print(e)

        #将text转换成html形式并自动补全内容
        try:
            html = etree.HTML(body, etree.HTMLParser())
            #解析html
            info = {"text":body, "html": html}
            return info;
            #返回html数据

        except ParseError as e:
            print("over")

    '''
    对list中内容进行筛选清除
    '''
    def content_clear(self, list):
        content = []
        for x in list:
            string = str(x)
            #判断是否为空
            if string is not None:
                #判断是否含有\n
                if '\n' not in string and '/' not in string:
                    #转换成str形
                    content.append(string)
        return content



    '''
    捕捉文本内容
    '''
    def content_catch(self, url):
        info = self.html_content(url)
        text = info["text"] #文本
        html = info["html"] #lxml中的html节点

        title = html.xpath('//head/title/text()')[0].strip()
        #获取到网页head内容

        meta = html.xpath('//head/meta[@name="description" or @name="Keywords"]/@content')
        #网页的描述信息和关键字

        #获取所有span中的内容
        span = self.content_clear(html.xpath('//span/text()'))
        #print(span)

        #获取所有a中的内容
        a = self.content_clear(html.xpath('//a/text()'))
        #print(a)


        #获取所有一级标签
        h1 = self.content_clear(html.xpath('//h1/text()'))
        #print(h1)

        #获取所有h5标签
        h2 = self.content_clear(html.xpath('//h2/text()'))
        #print(h2)

        #div标签
        div = self.content_clear(html.xpath('//div/text()'))
        # print(div)

        #p
        p = self.content_clear(html.xpath('//p/text()'))

        #标签
        keys = ["a","div","p","h1","h2","span","title","meta"]
        #标签列表
        values = [a, div, p, h1, h2, span, title, meta]
        #结果
        result = dict(zip(keys, values))

        print(result)
        #返回结果
        return result


    def getStringList(self, url):
        StringList = []
        content_list = self.content_catch(url)
        #获取关键码
        keywords = content_list.keys()
        for key in keywords:
            #获取每一个标签的list
            temp = content_list[key]
            #将list连接成字符串
            string = "/".join(temp)
            #将字符串添加到列表
            StringList.append(string)
        return StringList




# if __name__ == '__main__':
#     url = "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_6fb2d3471d3e4a8f8f4546cc380f276f"
#     #创建实例
#     H1 = HtmlContent()
#     #获取内容list
#     content_list = H1.content_catch(url)
#     #获取keys
#     keys = content_list.keys()
#     #创建捕捉关键词实例
#     ckc = ContentKeyCatch()
#     for key in keys:
#         #获取每一个标签的list
#         temp = content_list[key]
#         string = ""
#         print(len(temp))
#         string = "/".join(temp)
#         print(string)
#         #每一个链接进行关键词提取
#         keywords = ckc.string_catch(string, 10, True)



