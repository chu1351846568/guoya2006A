# from day02 import module_1
# from day02.module_1 import a as  module_1_a,name,test
#
# a ='我是模块02中的a变量'
#
# def name():
#     print('我是模块02中的name方法')
#
#
# class test():
#     name='我是模块02中的test类'
#
# print(a)
# name()
# print(test.name)

#字符串转列表 元组 集合
# t=(1,2,3,4,5,6,7,8,9)
# l=[1,2,35,25,4,78,9,62]
# s={1,2,3,4,5,8,97,25,63}
#
# print(list(b))
# print(list(t))
# print(tuple(l))
# print(set(t))
# print(list(s))

#字符串转数字
# a=123
# b='456'
# print(a+int(b))
#
# #数字转字符串
# print(str(a)+b)

#打开模式：r 读取  w清空写入 a追加写入  b二进制模式

# f=open('aaa.txt','w')#open打开文件
# f.write('hello kitty\nsdffgaf\nghgjfkr\n')#write写入内容至打开的文件
# f.readlines(['sdsfdg\n','dsfdgg\n','sdfsdgwere\n'])
# print(f.writable()) #判断是否可以写入
# f.close() #关闭文件

# f=open('aaa.txt','r')#open打开文件

# # print(f.read()) #默认读取全部数据
# # print(f.read(10)) #读取指定大小的数据
# # print(f.readline()) #按行读取，读取一行
# print(f.readlines())#按行读取，读取所有行
# # f.close()


a='asdsgfdhghjuhhkuyrt'
# # print(a[0])
# # print(a[-1])
# # print(a[1:-2])
# # print(a[1:-2:2])
# print(a[-1:0:-1])
# # print(a[::-1])
# # print(a[2:])
# # print(a[:-2])