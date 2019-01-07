# 第一种写法
# 1 打开
# 2 操作  (读/写)
# 3 关闭
f = open('1.text','w')         #1
# 参数1 file:文件路径
# 参数2 mode: 模式    (打开文件干什么)
#  r = read 读  读(默认) 读取整个文件      rb = readbytes = 读二进制
#  w = write 写(先清空再写入)              wb    =          写二进制
#  a = append 追加
# 参数3
# 参数4 encoding: 编码      (用哪种编码方式
f.write('nice to meet you\n')          #2            #  \n 换行
f.write('yes\n')
f.writelines(['a   ','b    ','c   '])    # 一次性写入多个数据
f.close()                       #3
# 读文件
h = open("2.text","r")
# content = h.read()        #读取整个文件, 若文件较大 会浪费内存
# content = h.read(5)       #分批读取,每次读5个
# content = h.readline()   #读取一行
content = h.readlines()     #读取所有行 返回一个列表
h.close()
print(content)

