#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import math
print math.sin(0)
#导入模块会相应地执行其中的代码,同时模块只有在第一次导入的过程中才会被执行
import sys;sys.path.append('/Users/wangshaoyu/python/learn');import Class;
nested=[[1,2],[3,4],[5,6]]
#如何调用模块中的方法，使用module.way
print list(Class.flatten(nested))
#__name__在主程序中__name__的值是__main__，而在模块中，这个名字是模块名如Class就是 Class
print __name__
#可以格式化的输出，如果数据结构过大，不能一行打印完，可以使用pprint模块中的pprint函数替代普通的print语句，
import pprint ;pprint.pprint(sys.path)
#解释器在列表中查找需要的模块，一开始sys.path就应该包含正确的目录，有两种方法可以保证系统搜索到你的目录：
#第一种方法是将你的代码放到合适的根目录的位置，第二种方法是告诉解释器去哪里查找需要的模块。
#标准的实现方法是在PYTHONPATH环境变量中包含模块所在的目录

#模块的三种导入方式
#import drawing 这一条语句之后，__init__模块的内容是可用的，
#import drawing.colors 这一条语句之后，可以通过全名drawing.colors来使用，
#from drawing import shapes 这一条语句之后，可以通过短名来使用 shapes
import copy
#print dir(copy) 
#可以使用dir来查看模块中所有的函数、类、变量
print [n for n in dir(copy) if not n.startswith('_')]
#copy 包中可以使用的所有特性__all__
print copy.__all__
#help(copy.copy)
#查看模块文档 print copy.__doc__
#快速查找到源代码的路径 print copy.__file__

#sys包中的介绍:
#argv：命令行参数，包括脚本名称 exit([argv])：推出当前程序，可以给定参数设置返回值的类型
#modules 映射模块名字到载入模块的字典  path：模块所在目录的目录名列表
#platform：平台标识符  stdin stdout stderr输入输出标准出错
print sys.argv
print sys.path,sys.platform

#os包 访问多个操作系统服务的功能
#environ：环境变量映射，可以通过environ['PYTHONPATH']访问  system(command)：执行操作系统命令如os.system('ls')   sep：路径中的分割符：/  pathsep:分割路径的分割符：是：
#linesep:行分割符  urandom(n):返回n字节的加密强随机数据

#time包 
#得到时间的秒 time()
#得到秒的日期元组  localtime(time())
#得到时间的字符串形式 asctime(localtime(time()))
#strptime(string[,format]) 将字符串解析为时间元组
#全球统一时间： gmtime(time.time())
#time.sleep() 等待多长时间
#datetime 支持日期和时间的换算  timeit:用来帮助开发人员对代码段的执行时间进行计时

#random模块
#random模块包括返回随机数的函数: random() :返回0-1之间的随机数   getrandbits(n):以长整型返回n个随机位
#		uniform(a,b):返回a-b之间的随机实数   randrange(start,stop,step) 返回range(start,stop,step)中的随机数
#choice(seq) ：从序列seq中返回随意元素    sample(seq,n) :返回其中随机的n个元素

















