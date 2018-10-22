from jieba import analyse
tifidf = analyse.extract_tags

class ContentKeyCatch(object):
    '''
    获取字符串集关键字
    '''
    def string_catch(self, string, number = 20, withWeight = False):   # 输入两个参数， 字符串， 需要返回的关键词数量
        keywords = tifidf(string, topK=number, withWeight= withWeight)
        for keyword in keywords:
            #打印权重值前topK的关键词
            print(keyword)
        print("-----------------------------------------\n")
        #返回关键词列表
        return keywords
