import os
import chardet

#获取文件目录的绝对路径
curr_dir = os.path.dirname(os.path.abspath(__file__))
#拼接路径
stop_words_path=os.path.join(curr_dir, 'stop_words.txt')
caution_words_path=os.path.join(curr_dir, 'caution_words.txt')
caution_words_replace_path=os.path.join(curr_dir, 'caution_words_replace.txt')
class ArticleFilter(object):
    def filter_replace(self, string):
        #存放禁用词和慎用词的列表
        stop_words = []
        caution_words = []



        #分别打开词库读取敏感字
        with open(stop_words_path,encoding='utf-8',errors='ignore') as stop_words_txt:
            lines = stop_words_txt.readlines()
            for line in lines:
                 # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
                 #type = chardet.detect(line)
                 #line = line.decode(type["encoding"])
                 stop_words.append(line.strip())
        with open(caution_words_path,encoding='utf-8',errors='ignore') as caution_words_txt:
            lines = caution_words_txt.readlines()
            for line in lines:
                caution_words.append(line.strip())

        # 输出过滤好之后的文章
        print("过滤之后的文字:" + self.replace_words(stop_words,caution_words, string))


    def replace_words(self,stop_words,caution_words, string):
        caution_words_replace=[]
        # 打开替换词库
        with open(caution_words_replace_path,encoding='utf-8',errors='ignore') as caution_words_replace_txt:
            lines = caution_words_replace_txt.readlines()
            for line in lines:
                caution_words_replace.append(line.strip())

        for words in stop_words+caution_words:
            if words in string and words in stop_words:
                string=string.replace(words, "*" * len(words))
            if words in string and words in caution_words:
                string=string.replace(words,caution_words_replace[caution_words.index(words)])

        return string





if __name__ == '__main__':
    while True:
        string = input("请输入一段文字:")
        run = ArticleFilter()
        run.filter_replace(string)
        continue