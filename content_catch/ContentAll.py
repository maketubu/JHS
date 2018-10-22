from content_catch.content_key_catch import  *
from content_catch.HTML_content_catch import *

class ContentAll(object):
    #关键码
    keywordslist = []
    #文字内容
    content = {}
    #内容字符串集合
    contentStringList = []
    #链接数
    link_num = 0
    #链接列表
    link = []
    #图片集
    pic = []
    #图片数
    pic_num = 0

    def __init__(self, url, key_number = 10, key_with_weight = False):
        #定义实例
        self.content = HtmlContent().content_catch(url)
        self.contentStringList = HtmlContent().getStringList(url)
        #循环获取每一个标签的string
        for string in self.contentStringList:
            keywords = ContentKeyCatch().string_catch(string, key_number, key_with_weight)
            #将keywords放进关键词集合
            self.keywordslist.append(keywords)

    #获取关键词
    def getKeywords(self):
        return self.keywordslist

    #获取文本内容list
    def getContent(self):
        return self.content

    #获取文本内容字符串集合
    def getContentStringList(self):
        return self.contentStringList

    #获取链接list
    def getLink(self):
        return self.link

    #获取链接数
    def getLinkNum(self):
        return self.link_num

    #获取图片lisk
    def getpic(self):
        return self.pic

    #获取图片数
    def getpicNum(self):
        return self.pic_num

