#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "string"#字符串可以使用序列的操作和方法（索引，分片，乘法，判断成员资格，求长度，最小值和最大值），但是字符串是不可变的
#字符串常用的方法有：find,split,lower,replace,strip,join
print "string".find("d")#返回最左端索引，如果没有找到返回－1
seq=['3','4','55','9']
print '/'.join(seq)#时split的相反函数，
print "String".lower()#返回小写的格式
print "st st good".replace('st','dd')
print "st st good".split()#程序默认使用所有空格作为分割符（其中包含了空格，制表，换行等）“string”.split('/') 可以自定义分割字符串
print "   dd".strip()#取出两侧空格的字符串

#创建和使用字典,字典中的键是唯一的，但是值可以不唯一，键可以使数字、字符串甚至是元组(其实就是任何不可变的类型)
phonebook={'Alice':'23415','Beth':'9012','Cecil':'3258'}
print phonebook['Alice']
#字典中常用操作 len(d),d[k],d[k]=v,del d[k],k in d

#字典中常用的方法，clear，copy(实现的是浅复制),，fromkeys,get,has_key，items和iteritems(迭代器)，keys和iterkeys,pop，update，values和itervalues
x={};y=x;x['key']='value';print y;x.clear();print y;#想清空原始字典总的所有元素，必须使用clear方法
#copy实现的是浅复制，将所有的键值对都复制一份，同时也包含了值里面的引用（因为进行的是浅复制）
x={'username':'admin','machines':['foo','bar','baz']};y=x.copy();y['username']='m1h';y['machines'].remove('bar');print y;print x
#同时也可以使用深复制,这样的话，引用所指向的值也被复制了，自然对x修改不会影响到对y的修改。
from copy import deepcopy;x={'username':'admin','machines':['foo','bar','baz']};y=deepcopy(x);y['username']='m1h';y['machines'].remove('bar');print y;print x
x={}.fromkeys(['name','age']);print x;y=dict.fromkeys(['name','age'],False);print y#可以对给定的键建立新的字典，每个键默认的值为None，也可以进行设置
#get方法可以提供更好地访问字典项的方法，如果字典中不存在元素，使用d['key']就会报一个错误，使用get则会返回一个None
d={};print d.get('name','t')#也可以设置默认返回值
#has_key和 k in d 起到一样的效果，两种方法都可以，如d.has_key('name')和 ‘name’ in d等价
d={'title':"python web site",'url':'http://www.baidu.com'};print d.items()
it=d.iteritems(); print list(it)#使用迭代器更加便利
#keys 和iterkeys跟items一样‘
d={'x':1,'y':2};d.pop('x');print d#pop方法用来获得对应的给定键的值，然后将键值对删除掉
#update方法利用一个字典项更新另一个字典,如果x中存在的，值就是x中的值，如果不存在，则是用d中存在的值
d={'title':'pytho web site','url':'http://www.python.org','change':'mar 14 22:09:15 MET 2008'}
x={'title':'python language website'}
d.update(x)
print d;print d.values();it=d.itervalues();print list(it)

#print的用法
print 'hello'+',','kdk'
#变量赋值
x,y=1,2;y,x=x,y;print y
x={'name':'wang','password':'123456'};key,value=x.popitem();print key,value