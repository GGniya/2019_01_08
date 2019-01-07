# #字典  dictintary
# 1创建
a={}   # a=[]
b=dict()  #a = list()
# c = [zhangsan,20,郑州]
c={
    'name':'zhangsan',
    'age':'23',
    'address':'郑州',
}
print(c)
# 2添加/更新
# 如果key不存在就是添加,存在就是更新
# a.append()    a.insert()   #列表添加
c['sex'] = '男'              #字典添加
c['name'] = 'lisi'           #更新
print(c)
# 3 删除
# a.pop()   a.remove()                          #列表删除
c.pop('name')
 #参数1:k=key 删除的字典的字段
# c.pop('phone')                    #删除的字段不存在则会报错: keyError
c.popitem()                         #默认删除字典的 随机 一个字段  如果字典已经为空则会报错
del c['age']                        #强制删除
print(c)
# 4查找元素
# 'zhangsan' in ['zhangsan','list']       #列表查找
print('age' in c)
print('phone' in c)
print('age' in c.keys())       #等价于 print('郑州' in c.keys())
print('郑州' in c.values())

# 5获取
# a[3]
# name = c['address'] #不存在会报错   不推荐
name = c.get('address')       #推荐
#参数1 k= key
#参数2 default 默认值为None,     null = none = nil
print(name)
# 6 字典遍历
#    for    循环

# # 不推荐写法
# for key in c:
#     value = c.get(key)
#     print(key,value)
# 推荐
for key,value in c.items():
    print(key,value)