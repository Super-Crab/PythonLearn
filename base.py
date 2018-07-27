#!/usr/bin/python
#coding:utf-8

message = "hello world python"
print (message)

# 首字母大写
# \t 表示空格 \n表示换行
name = 'ada \t love \nlace'
print (name.title())

# 转化为大写
print (name.upper())

# 转化为小写
print (name.lower())

msg = ' python '
# 删除末尾的空白
print (msg.rstrip())

# 删除头部的空白
print msg.lstrip()

# 删除字符串两端的空白
print msg.strip()

# 访问列表元素
bicycles = ['trek', 'cannondale', 'redkine', 'sprcialized']
print bicycles
print bicycles[0]

# 修改列表元素
names = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print names

names[0] = 'zhangsanfeng'
print names

# 在队尾添加元素
names.append('qianda')
print names

# 在列表中插入元素
names.insert(0 , 'qianer')
print names

# 删除元素
del names[1]
print names

# 将列表中第四个元素出栈
poped_names = names.pop(3)
print poped_names
print names

# 根据值删除元素
names.remove('lisi')
print names

nicks = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print nicks

# 按照字母排序,会改变原始数据位置
nicks.sort()
print nicks

# 按照字母顺序相反排序
nicks.sort(reverse = True)
print nicks

# 按照字母排序，不改变原始数据
print sorted(nicks)
print nicks
print sorted(nicks, reverse = True)

# 倒叙列表
nicks.reverse()
print nicks
# 确定列表长度
print len(nicks)

# -1 代表最后一个元素 -2代表倒数第二个元素
print nicks[-1]
print nicks[-2]


# 遍历整个列表

for nick in nicks:
    print nick
    print nick.title() + " , welcome to china"
print "print all message and print finish!"

# range 函数
print range(1, 5)
for value in range(1, 5):
    print value
numbers = list(range(1, 5))
print numbers


squares = []
numbers = range(1, 11)
for number in numbers:
    squares.append(number ** 2)
print squares

# 数据大小比较
print min(squares)
print max(squares)
print sum(squares)

# 切片
nicks =['zhangsan','lisi','wangwu','zhaoliu']
# 截取 0，1，2
print nicks[0:3]
# 截取 2
print nicks[2:3]
# 截取2 到最后一个
print nicks[2:]
print nicks[4:]
print nicks[:2]
print nicks[:]
print nicks[-2:]

# 列表拷贝
# 深拷贝  指向不同的地址
nicks =['zhangsan','lisi','wangwu','zhaoliu']
nicks_copy = nicks[:]

nicks.append('zhangsanfeng')
nicks_copy.append('zhangwuji')

print("original nicks")
print(nicks)

print("copy nicks")
print(nicks_copy)

# 浅拷贝 指向相同的内存地址
nicks =['zhangsan','lisi','wangwu','zhaoliu']

nicks_copy = nicks;

nicks.append('zhangsanfeng')
nicks_copy.append('zhangwuji')

print("original nicks")
print(nicks)

print("copy nicks")
print(nicks_copy)

# 元祖
# python将不能修改的值成为不可变的，不可变的列表成为元组，元组使用圆括号来标识

points = (200,50,300,90)
print(points[0])
print(points[1])
print(points[2])
print(points[-1])

for point in points:
    print point

points = (1, 2, 3, 4)
for point in points:
    print point

# 字典
alien_0 = {'color' : 'green', 'point' : 5}
print alien_0
print alien_0['color']

alien_0['x_point'] = 250
alien_0['y_point'] = 100
print alien_0

alien_0 = {}
alien_0['x_point'] = 250
alien_0['y_point'] = 100
print alien_0
# 删除键值对
del alien_0['x_point']
print alien_0

# 遍历所有的键值对

values = {'1':'one','2':'two','3':'three','4':'four'}
for value in values.items():
    print value

# 注： 第一个在前面的是key 后面的是value
for key,value in values.items():
    print "\n key :" + key
    print "value :" + value

for value,key in values.items():
    print "\n key :" + key
    print "value :" + value

# 遍历字典中所有的键
for value in values.keys():
    print value

# 遍历字典中所有的值
for value in values.values():
    print value


number = int(10)
begin = int(0)
while begin <= number:
    print begin
    begin += 1

# 无参的函数
def greet_user():
    print "Hello Python"

greet_user()

# 有参的函数
def greet_user(username):
    print "Hello Python: " + username

greet_user('kobe')
greet_user("111")

# 通过位置确定实参
def describe_pet(animal_type,pet_name):
    print "I have a " + animal_type + "."
    print "My " + animal_type + "'s name is " + pet_name.title() + "."

describe_pet('dog', 'james')
describe_pet('dog', 'iverson')

# 关键字实参
describe_pet(pet_name = 'kkkk', animal_type = 'cat')

# 默认值实参
def describe_pet2(animal_type,pet_name = 'kkkk'):
    print "I have a " + animal_type + "."
    print "My " + animal_type + "'s name is " + pet_name.title() + "."

describe_pet2('cat')

# 返回值
#1.返回简单值

def get_formatted_name(first_name,last_name):
    full_name = first_name + '-' +last_name
    return full_name.title()

musician = get_formatted_name('kobe','bryant')
print musician

#2.让实参变成可选的
def get_formatted_name(first_name,last_name,middle_name= ''):
    """返回整洁的姓名"""

    if middle_name:
        full_name = first_name +'-'+middle_name+'-'+last_name
    else:
        full_name = first_name + '-' +last_name

    return full_name.title()

musician = get_formatted_name('kobe','bryant')
print(musician)

musician = get_formatted_name('kobe','bryant','vboy')
print(musician)

#