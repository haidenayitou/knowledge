#!/usr/bin/env python
#! -*- coding: utf-8 -*-
name = 'wang'
if name.endswith('xng'):
	print 'hello,mr wang'
elif name.endswith('ang'):
	print 'hello ,elif'
else:
	print 'hello nihao!'
#python 中的比较运算符 x is y (x 和 y 是否为同一个对象) x is not y(x 和 y是不同的对象) x in y  和x not in y
x=7;y=x; print x is y 
#while 
x=1
while x<=100:
	print x
	x+=5
x=[1,3,4,5,6]
for key in x:
	print key
#range 函数,包含下限不包含上限
print range(0,10)
#对字典进行遍历,遍历的过程中时无序的
x={'name':'wang','passord':'123456'}
for key,value in x.items():
	print key ,value
#zip 迭代函数,将两个序列压缩在一起，然后返回一个元组的列表
names=['anne','beth','george','damon']
ages=[12,45,32,102]
print zip(names,ages)
#编号迭代,index返回编号，string返回值
for index, string in enumerate(names):
	print index ,string
#列表推导式
y=[x*x for x in range(1,10,2)];print y
#pass delete (删除的只是列表的名称而不是本身)

import math; print callable(math.sqrt)#内建的callable函数可以来判断函数是否可以调用
def hello(name):
	'这是一个hello函数'＃这是函数文档，给函数添加文档字符串
	print 'hello '+name+'!'
	return 'lalala'
print hello('wang')

