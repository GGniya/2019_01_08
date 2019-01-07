f=open("movie.csv","w", encoding="utf-8")
# utf-8 通用编码            pycharm默认格式
# gb18030   中文编码         Windows系统软件大都采用

f.write("蜘蛛侠,33039,http://www.baidu.com\n")
f.write("蜘蛛侠1,33409,http://www.baidu.com\n")
f.write("蜘蛛侠2,33609,http://www.baidu.com\n")
f.write("蜘蛛侠3,33809,http://www.baidu.com\n")
f.close()