#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "nihao"
#kdkkd
#user_name=raw_input("what name is")
#print user_name
print str(1000L)
print repr(1000L)
print '''kfld
lk;fk;dkl
'''
#python提供六种序列 包含了列表，元组，字符串，Unicode字符串，buffer对象，xrange 对象#
#同时提供了映射
#列表可以修改，元组不可以修改
edward=['edward',42]
john=['john',42]
database=[edward,john,edward,john]
print database
#索引
print database[0]
#分片,第一个索引是需要提取部分的第一个编号, 第二个索引是表示剩余元素的第一个索引，第三个参数表示步长
print database[0:1]
print database[::2]
#步长可以为负数，表示从右往左进行遍历
print database[::-1]
#序列是可以相加的
print database+database
#None 通常表示这里什么都没有，如果想初始化，则可以初始化一个10个的空列表
sequence=[None]*10
print sequencese
sequence[5]="ff"
print sequence
#使用in运算符判断某个条件是否为真
print "ff" in sequence 
print "d" in sequence
print ["edward",42] in database
#此外有min max len这三个内建函数
print min(sequence)
print max(sequence)
print len(sequence)
#基本的列表操作：元素赋值、删除元素、分片赋值、
x=[1,1,2]
x[1]=3
print x
del x[2]
print x
x[1:]=[3,4,5]
print x
#分片赋值可以在不需要替换任何元素的情况下插入新的元素
number=[1,5]
number[1:1]=[8,8,9]
print number
#列表有哪些方法:append ,count,extend,index,insert,pop,remove,reverse,sort
print list(number)
number.append(9);print number #向列表后面添加一个元素;
print number.count(8) # 统计8出现的次数
number.extend(x);print number #在列表后面一次添加多个元素，修改了number元素
print number.index(9);#print number.index("dd") 返回匹配元素的第一个索引位置，当搜索不到的时候会引发一个异常
number.insert(4,6);print number #将对象插入到列表中,和 number[4:4]=6等价
number.append(number.pop()); print number#可以使用append和pop实现栈的入栈和出栈操作,pop会返回出来的元素
number.reverse();print number
number.sort();print number #sort对其进行排序，默认使用升序进行排序
number.sort(reverse=True);print number 


##元组 和列表一样都是一种序列，但是元组不能更改，列表可以更改，使用()
print 3*(40,)#只有一个值，表示元组必须有一个逗号
print tuple([1,2,3])#将目标转换为元组
#元组存在的两个重要的意义1，元组可以在映射中当作键使用，而列表不行 2，元组一般作为很多内建方法的返回值存在






















