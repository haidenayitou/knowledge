#!/usr/bin/env python 
#! -*- coding: utf-8 -*-

class Person:
	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name
	def greet(self):
		print "hello world!"+self.name
	def __inaccessible(self):
		print 'bet yu can\'t see me!'
	def accessible(self):
		print 'te secret message is'
		self.__inaccessible()
#self 一般是实例作为self也就是函数第一个参数
foo=Person()
foo.setName('wang')
print foo.getName()
foo.greet()
print foo.name
#为了让方法或者特性变为私有的（外部无法访问），只要在它的名字前面加上双下划线就可以了，
#但其实在类的内部定义中所有已双下划线开始的名字都被翻译成为前面加上单下划线和类名的形式
foo._Person__inaccessible()

#两个都达到同样的效果
def foo(x):return x*x
y=lambda x:x*x
print y(4);print foo(4)

#继承
class Filter:
	def init(self):
		self.blocked=[]
	def filter(self,sequence):
		return [x for x in sequence if x not in self.blocked]
#继承的用法
class SPAMFilter(Filter):
	def init(self):
		self.blocked=['SPAM']

f=Filter()
f.init()
print f.filter([1,2,3])
s=SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','egg'])
#print random.choice([1,2,3])
#判断一个类是否是另一个类的子类,__bases__用来描述所有的父类,__class描述属于哪个类,hasattr用来查看这个对象是否有这个方法
print issubclass(SPAMFilter,Filter);print SPAMFilter.__bases__;print s.__class__;print hasattr(s,'filter')
#多重继承childClass(father1,father2)


#构造方法 __init__ 析构函数__del__不能确定什么时候调用所以一般不要使用
class Bird(object):
	def __init__(self):
		self.hungry=True
	def eat(self):
		if self.hungry:
			print 'aaaaaa'
			self.hungry=False
		else:
			print 'No thandks'
class songBird(Bird):
	def __init__(self):
		#Bird.__init__(self)#必须要进行初始化
		super(songBird,self).__init__()
		self.sound='squawk'
	def sing(self):
		print self.sound
	@staticmethod#静态方法必须添加一个标注
	def makeStatic():
		print 'it is a static method'

sb=songBird()
sb.sing()
sb.eat()
songBird.makeStatic()

#yield 生成器,生成器是一个包含yield关键字的函数，当它被调用的时候，在函数体中的代码都不会被执行，
#而会返回一个迭代器，每次请求一个值，就会执行生成器中的函数，直到遇到一个yield或者return语句。
#yield 语句意味着要生成一个值，return语句意味着生成器要停止执行。
def flatten(nested):
	for sublist in nested:
		for element in sublist:
			yield element
nested=[[1,2],[3,4],[5,6]]
print list(flatten(nested))

#遍历任意层次的数组
def flatten(nested):
	try:
		#当然如果序列中包含一个字符串，则会出现无穷递归,所以将字符串当作原子类型对待
		try:
			nested+''
		except TypeError:pass
		else:raise TypeError
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested

nested.append([4,5,6,[5,6]]),nested.append(['stirng','stirng'])
print list(flatten(nested))

#property函数,应该尽量使用property函数而不是访问器方法
class Rectangle:
	def __init__(self):
		self.width=0
		self.height=0
	def setSize(self,size):
		self.width,self.height=size
	def getSize(self):
		return self.width,self.height
	size=property(getSize,setSize)
r=Rectangle();r.width=0.9;r.height=0.8;print r.size;print r.size;r.size=9,0.9;print r.size
print __name__










