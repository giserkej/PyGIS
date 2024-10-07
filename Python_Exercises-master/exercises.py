# print('hello kejin')
# r原生字符串默认取消转义

# a = 666
# b = 999
# if a > b:
#     print(a > b)
# else:
#     print(a > b)

# 逻辑运算符
# and or not
# a = 'hh'
# b = 'heihei'
# if a and b:
#     print(True)
# start_index = 1
# while start_index <= 100:
#     print('nihao')
#     start_index += 1
# print('打印完毕')

# while True:
#     print('永远18岁')

# i = 1
# count = 0
# while i < 100:
#     count += i
#     print('这是第%d次循环，此时的i为%d，此时的count为%d' %(i, i, count))
#     i += 1
# print('循环结束，此时的总数为：', count)

# 九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         count = i * j
#         print('%d x %d = ' %(i, j), count, end='\t')
#         j += 1
#         if i < j:
#             break
#     i += 1
#     print('\r')

# str = 'helloPython'
# for i in str:
#     print(i)

# range函数可以用来充当计数器，range函数包前不包后原则
# 用range函数输出1到100的和
# number = range(1, 101, 1)
# count = 0
# for i in number:
#     count += i
# print(count)

# a = 'hello'
# print(type(a))
# b = a.encode()
# print(b)
# print(type(b))

# list反转
# list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# list2 = []
# 方法一：用sorted方法，reverse为true
# list2 = sorted(list1, reverse=True)

# 方法二：用reversed方法
# list2 = reversed(list1)
# print(list2)

# 方法三：设置数组的步长为-1
# list2 = 'abcdefghijklmnopqrstuvwxyz'
# print(list1[::-1])

# st = 'hello python'
# print(st.split('l'))

# remove pop del三种删除元素的方式
# remove删除对象，pop删除索引

# sort和reverse都是排序，sort正序，reverse倒序
# li = [1,4,3,5]
# li.reverse()
# print(li)

# li = ['a', 'c', 'd']
# li.reverse()
# print(li)


# list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# list1.reverse()
# print(list1)


# li1 = [1, 2, 3, 4, 5, 6]
# li2 = li1
# print(id(li1))
# print(id(li2))

# 浅拷贝，一般用的比较多
# import copy
# li1 = [1, 2, 3, 4, 5, 6]
# li2 = copy.copy(li1)
# print(li1, id(li1))
# print(li2, id(li2))
# li1.append(7)
# print('==================================')
# print(li1, id(li1))
# print(li2, id(li2))


# def fun_a(x, y):
#     return x + y
# b = fun_a(100, 200)
# print(b)

# import builtins
# print(dir(print))


# map #对list中的每一个元素都进行运算
# list1 = [1, 2, 3, 4]
# def multiple(x):
#     return x * 2
# list2 = map(multiple, list1)
# list2 = list(list2)
# print(list2)

# reduce 两个元素之间进行运算，之后再与后面的元素依次进行运算
# from functools import reduce
# list1 = [1, 2, 3, 4]
# def func(x, y):
#     return x * y
# res = reduce(func, list1)
# print(res)


# import module
# print(module.name)
# print(module.func())

# from module import func
# print(func())

# 包就是含有__init__.py的文件夹/目录
# __init__.py的作用就是导入包内的其他模块


# 递归函数
# 递归函数实现累加，在递归中如果出现int和nonetype不能参与计算的情况，一般是情况没有写全，少了某种情况；

# def add(x):
#     # if x == 1:
#     #     return 1
#     if x > 1:
#         x = x + add(x - 1)
#         return x
#     else:  # 如果不写else的情况，会导致在x = 1的时候出现x - 1 = 0的情况，0带入函数会导致不符合任何情况进而无返回值
#         return x
# print(add(100))


# 递归函数实现斐波那契额数列
# import time
# time0 = time.time()
# def feb(x):
#     if x >= 2:
#         return feb(x - 2) + feb(x - 1)
#     else:
#         return x
# print('斐波那契额数列第%s个数值是：%s' %(40, feb(40)))
# time1 = time.time() - time0
# print('用时：%s秒' %time1)

# 装饰器是闭包的一种，说白了就是在不修改源代码的基础上，实现功能的新增。首先要定义一个函数，然后在原函数内添加一个形参，并且调用这个形参函数，装饰器的意思就是内函数的一个装饰。


# class Washer:
#     height = 800
#     width = 400
#     def wash(self):   # self表示调用该方法的对象
#         print('洗衣服')

# washMachine = Washer()
# washMachine.wash()
# height = washMachine.height
# print(height)

# 面向对象三大特性：封装 继承 多态
# 封装的定义：将不希望被外界访问的属性和方法隐藏起来，称为封装
# 封装的格式：在属性或者方法前添加两个下划线__
# 如果在继承中子类需要对父类的方法进行重写或者扩展，可以在子类的同名方法中用super().方法名的方法，或者是父类.方法名的方法来实现


# 文本处理：
# 打开文件 -- 读写文件 -- 关闭文件
# 打开文件：open()            读写文件：read() write()            关闭文件：close()
# 属性有：文件名.name 返回文件名称以及具体路径    文件名.mode 返回文件的返回模式  文件名.closed   返回文件是否关闭


# 文件有开必有关
# f = open(r'D:\PyExcs\kejin.txt', mode='r+')
# print(f.name)
# print(f.mode)
# print(f.closed)
# readlines = f.read()
# print(readlines)
# f.write('\n你好，这里是南宫')
# f.tell()
# f.close()

# 打开文件的方式可以使用with open(file, mode) as f的方式来写，这样的话就避免了忘记写close的情况



# 图片赋值
# 读取文件
# with open(r'D:\PyExcs\picture.jpg', 'rb') as f:
#     img = f.read()
#     print(img)

# with open(r'D:\PyExcs\图片.jpg', 'wb') as f:
#     f.write(img)

# os模块 os.rename(old name, new name)重命名    os.remove(file)删除文件     os.mkdir()创建文件夹    os.rmdir()删除文件夹    os.getcwd()获取当前所在目录     os.getlistdir()获取当前文件夹中的所有文件
# import os
# print(os.getcwd())
# print(os.listdir())

# os.rename('./Python_Exercises-master/first.py','./Python_Exercises-master/exercises.py')

# 可迭代对象
# from _collections_abc import Iterable
# str = '123456'
# res = isinstance(str, Iterable)
# res2 = isinstance(12345, int)
# print(res)
# print(res2)

# 可迭代对象不一定是迭代器对象，但迭代器对象一定是可迭代对象；如果要将可迭代对象转换为迭代器对象，可以使用iter方法


# 生成器：一边循环一边生成的自定义迭代器，称为generator  有yield关键字函数就是生成器函数


# li = []
# x = int(input('你输入次数:'))
# def appendA():
#     li.append('a')
# for i in range(x):
#     appendA()
# print(li)

# 线程
# import threading
# import time

# # 定义全局变量

# def wData():
#     for i in range(5):
#         li.append(i)
#         # time.sleep(1)
#     print('写入的数据是：',li)

# def rData():
#     print('读取的数据是：', li)

# if __name__ == '__main__':
#     li = []
#     time0 = time.time()
#     # 创建子线程
#     t1 = threading.Thread(target=wData)
#     t2 = threading.Thread(target=rData)
#     # 开启线程
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()
#     time1 = time.time() - time0
#     print('用时%f秒'  % time1)

# 线程同步
# 有两种方式，一种是线程等待（阻塞），也就是join；第二是互斥锁。互斥锁就是对共享数据进行锁定，保证同一时刻只有一个线程在访问数据。但是注意，上锁必须解锁，否则会形成死锁。上锁acquire()，解锁release()


# 队列间通信 q.put()放入数据  q.get()获取数据     q.empty()队列是否为空   q.qsize()返回当前消息数量   q.full()判断队列是否已满
# import queue
# q = queue.Queue(3)

# q.put('爱你到老')
# q.put('你在做梦')
# q.put('爱在深秋')
# print(q.qsize())
# print(q.get()) # 获取队列中的一条消息，并从队列中移除
# print(q.get())
# print(q.get())
# print(q.full())
# print(q.empty())

# import multiprocessing
# from multiprocessing import Process, Queue
# import time
# li = ['张三','李四','王五','赵六','柯七']
# # list1 = []
# def wdata(q1):
#     for i in range(30):
#         print(f'{i}已经被放入')
#         q1.put(i)
#         time.sleep(0.2)
# def rdata(q2):
#     # list2 = []
#     while True:
#         if q2.empty():
#             break
#         else:
#             # for i in list1:
#             print('取出队列，',q2.get())
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=wdata, args=(q,))
#     p2 = Process(target=rdata, args=(q,))
#     p1.start()
#     p1.join()
#     # print(list1)
#     p2.start()
#     p2.join()


# from multiprocessing import Queue
# q = Queue()
# q.put('你好')
# print(dir(q))

import gevent
import time
def sing():
    print('在唱歌')
    gevent.sleep(1)
    print('唱完歌了')
def dance():
    print('在跳舞')
    gevent.sleep(1)
    print('跳完舞了')
if __name__ == '__main__':
    # 创建协程对象
    gs = gevent.spawn(sing) # 创建协程对象
    gd = gevent.spawn(dance)

    gs.join()
    gd.join()
    # gevent.sleep() # 耗时操作
    # gevent.joinall() # 等所有协程对象执行完毕之后主程序再退出