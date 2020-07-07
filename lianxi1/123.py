# a=25
# b=20
# print (a+b)
#
# a = 1,2,3,4,5
# print(a)
#
# a,b,c = [1,2,3]
#
# print(a)
# print(b)
# print(c)
#
#
# x,y,* z = (1,2,3,4,5)
#
#
# print(x)
# print(y)
# print(z)
#
# a = 5
# b = 6
# c = a + b
#
# print(c)
#
# a = 5
# b = 6
# c = a - b
#
# print(c)
#
#
# a = 5
# b = 6
# c = a * b
#
# print(c)
#
# a = 5
# b = 6
# c = a / b
#
# print(c)
#
# a = 5
# b = 6
# c = a % b
#
# print(c)
#
# a = 5
# b = 6
# c = a ** b
#
# print(c)
#
# a = 5
# b = 6
# c = a // b
#
# print(c)
#
# z = 15264
# print(z % 100)
#
# z = z // 100
# print(z)
#
# print(z % 100)
#
#
# l = ["老干妈","腾讯","百度"]
#
# if ("果芽" in l):
#     print("合作方")
#
# else:
#     print("非合作方")
#
#
# z = 13596
#
# z = z // 1000
# print(z)
#
# print(z % 10)
#
#
# sc = 59
# if (sc > 0 and sc < 60):
#     print("不及格")
# elif (sc >= 60 and sc <= 70):
#     print("及格")
# elif (sc >=71 and sc <= 80):
#     print("良好")
# elif (sc >= 80 and sc <= 100):
#     print("优秀")
# else:
#     print("请输入正确的成绩")
#
#
# sc_1 = [40,80,70,60,95,82,75,74,98]
# for sc in sc_1:
#  if (sc > 0 and sc < 60):
#     print("不及格")
#  elif (sc >= 60 and sc <= 70):
#     print("及格")
#  elif (sc >=71 and sc <= 80):
#     print("良好")
#  elif (sc >= 80 and sc <= 100):
#     print("优秀")
#  else:
#     print("请输入正确的成绩")
#
#
#
#
#
#
# f = True
# a = 17
#
# while f:
#     b = int(input("请输入正确的数字"))
#     if b > a:
#         print ("大了")
#     elif (b < a):
#         print("小了")
#     else:
#         print("恭喜你")
#         f = false
#
# a = 1
# for i in range(10,0,-1):
#    # print(i)
#    a *= i
#    print(a)
#
#
# sc = [40,52,60,82,89,90,98]
# for s in sc:
#  if (s>0 and s<60):
#       print("不及格")
#  elif (s>=60 and s<70):
#      print("及格")
#  elif (s >= 70 and s < 80):
#     print("良好")
#  elif (s >= 80 and s <= 100):
#     print("优秀")
#  else:
#         print("请重新输入成绩")

#找出100以内可以被3整除的数字
#
# for i in range (1,100):
#     if (i % 3!= 0 ):
#         continue
#     print(i)

# for i in range (1,100):
#     if ( i % 3 != 0):
#           continue
#     # print(i)

# 定义一个求两个数商和余数的方法
#
# a = 10
# b = 5
# c = a // b
# print(c)
#
# a = 6
# b = 5
# c = a % b
# print(c)


# 定义一个求两个数商和余数的方法
# a=10
# b=2
#
# def  shang_yu( a, b ):
#     print("商:",a//b, ",余数:",a % b)

#
# shang_yu(10,2)
#
# shang_yu(20,3)




# 定义一个求两个数商和余数的方法

# def  shang_yu ( a, b ):# a,b形参
#      if(b == 0):
#          return  None   #return 返回值
#      else:
#          return (a//b,a%b)

# # res=shang_yu(20,6) #按照位置传参
# res=shang_yu(b=6, a=20) #按照关键字传参
# print(res)
# if res is None:
#     print("参数错误")
# else:
#     print("商:",res[0],"余数为:",res[1])

# 魔法赋值
# c = 1,2,3,4,5
# a,*b = (1,2,3,4,5)
# print(b)
# def suml(*args):
#     s = 0
#     for i in args:
#         s = s + i
#
#         return s
# print(suml(1,2,3,4,5,6,7,8,9,10,56,87,56,45,52))


# print(b)
#
# def suml(*args): # *args接收动态位置参数，**kwargs 接收动态关键字参数
#     print(args)
#     s=0
#     for i in args:
#      s=s+i
#     return s
#
# print(suml(1,2,3,4,5,6,7,8,9,10,56,87,56,45,52))

# l = 1,2,3,4,5,6,7,8,9,10,56,87,56,45,52
# sum1 = 0
# for i in l:
#    sum1 += i
#
# print(sum1)


# def suml(stu,*args,**kwargs): # *args接收动态位置参数，**kwargs 接收动态关键字参数
#
#     return (stu,args,kwargs)
#
# print(suml('菜花',1,'老薛',2,1,3,name='xue',age=18))


#面向对象
# class cc():
#     a=None
#     b=None
#     rss = None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def xx(self):
#         self.rss=self.a+self.b
#     def ss(self):
#         self.rss=self.a/self.b
#     def zz(self):
#         self.rss=self.a*self.b
#     def get(self):
#         print(self.rss)
#
# c=cc()
# c.input(10,20)
# c.xx()
# c.get()
# c.zz()
# c.get()


#面向对象
# class calc():
#     a=None
#     b=None
#     res = None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.rss=self.a+self.b
#     def div(self):
#         self.rss=self.a/self.b
#     def cheng(self):
#         self.rss=self.a*self.b
#     def get(self):
#         print(self.rss)
#
# c=calc()
# c.input(10,20)
# c.sum()
# c.get()
# c.div()
# c.get()
# c.cheng()
# c.get()




# class calc():
#     res = None
#     def __init__(self,a,b): #魔法函数，类实例化的时候调用，又称构造方法
#         self.a=a
#         self.b=b
#
#     def sum(self):
#         self.rss=self.a+self.b
#
#     def div(self):
#         self.rss=self.a/self.b
#
#     def cheng(self):
#         self.rss=self.a*self.b
#
#     def get(self):
#         print(self.rss)
#
# c=calc(29,39)
# c.sum()
# c.get()
# c.div()
# c.get()
# c.cheng()
# c.get()


# 九九乘法表
# for i in range(1,10,1):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="\t")
#     print()
#
# 通过占位符格式化
# for i in  range(1,10):
#     for j in  range(1,i+1):
#         print('%d X %d = %d'%(j,i,i*j), end ='\t')
#     print()
#
# .format
# for i in  range(1,10):
#     for j in  range(1,i+1):
#      print('{} X {} = {}'.format(j, i, i * j), end='\t')
#     print()

# l = [1,2,3,4,6,8,7,5,26,41,25,20,18,16,17,21,25]
#
# length = len(l)
# for  i in range(length-1,0,-1): #外层循环确定排好序的数据下标
#      for j in range(i): #遍历未排序的列表
#          if (l[j]> l[j+1]):  #判断相领两个数据，前边的如果大于后边的，则交换两个数据的位置
#             l[j],l[j+1]= l[j+1],l[j]
# print(l)

# #继承
# class parent():
#
#     money = 10000000
#     house = 20
#     __yi_wu ='裤子'
#
#     def shou_yi(self):
#         print('点石成金')
#
# class Child(parent):
#             ai_hao = '花钱'
#             def __init__(self,*args,**kwargs):
#                 super().__init__(*args,**kwargs)
#                 def shou_yi(self):
#                     print('影分身之术')
#             # pass
# c = Child()
# print(c.money)
# print(c.house)
# print('点石成金')

# class aaa():
#
#     pub_res = '公有变量'
#     __pri_res = '私有变量1'
#     _pri_res ='私有变量2'
#
#     def pub_function(self):
#         print('公有方法')
#     def _pri_function(self):
#         print('私有方法1')
#     def _pri_function(self):
#         print('私有方法2')
#
#
# print(aaa.pub_res)
# print(aaa._pri_res)
# print(aaa().pub_function())
# print(aaa()._pri_function())


#
# l=[1,2,3,4,5,6,7,8,9]
#
# l[0]=20
# print(l)
# l[1:5]=[30,40,50,60]
# print(l)
#
#
#
# print('{:,}'.format(100000000))
# print('{:^10}'.format(123))
# print('{:.3f}'.format(2.3455688799887))

#添加
# l=[1,2,3,4,5,6,7,8,9,80]
# l.append('王大锤')
# l.append('王大锤')
# l.insert(1,'瓦罐降')
# print(l)
#
#
# #删除
# print(l.pop())   #根据下标删
# print(1)
#
# print(l.pop(1))   #根据下标删
# print(1)
#
# l.remove(3)   #根据内容
# print(1)
#
# l=[2,3,4,5,67,8]
# l.remove(4)
# print(l)
#
#
#
# l=[True,1,2,3,4,5,6]#python true l false 0
# l.remove(1)
# print(l)
#
# l=[False,1,2,3,4,5,6]#python true l false 0
# l.remove(1)
# print(l)
#
#
# l.clear()
# print(l)
#
# #排序
# # a=[5,6,7,8,9,10,52]
# # a.sort(reverse=true)
# # print(a)
#
#
#
# #字典添加
# d={'name':'小明','age':18,'sex':'女'}
#
# print(d.items())
#
# for k ,v in d.items():
#     print(k,v)
#
#
# print(d.pop('addr'))
# print(d)
#
# s={}
# for key in  d:
#     if key.startswith('a'):
#         continue
#     s[key]=d[key]
#  print(s)

#
# def div(a,b):
#     try:
#         return  a/b
#     except:
#         return
# print(div(0,20))

#
#
# def div(a,b):
#     try:
#         return  a/b
#     except:
#         return
# print(div(1,0))




class CustomException(Exception):
    def __init__(self,value='值不能为0'):
        self.value=value
        def _str_(self):
            return  self.value

a = 0
try:
    if a==0:
        print('a={ } 触发异常'.format(a))
        raise  CustomException
    print('a={ } 未触发异常'.format(a))
except CustomException as e:
    print(e)

sdfsfgdsghgkjhlkserertrt

12312313123123131313