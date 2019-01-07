f = open("2.text", "r")
content = f.read()
# 字符替换
content = content.replace(',', '').replace('"', "").replace(".", "").replace("!", "").replace("\n", "").replace("?", "")
content = content.lower()      #把字母统一转换程小写    大写-- upper
words = content.split(" ")
# print(words)
# #   利用字典表现单词个数
# word_count = {}
# for word in words:                    #遍历获得单词
#     if word in word_count:             #判断单词是否在字典中
#         word_count [word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)
# 调用python包统计
from collections import Counter
word_count = Counter(words)
top_10 = word_count.most_common(10)      #词频前10
print(word_count)
print(top_10)



