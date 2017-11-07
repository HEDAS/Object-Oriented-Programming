class JNU(object):
	'''***这是个新的暨南大学类***'''

	time='7:30-22:00'
	def __init__(self,new_time='7:30-22:30',library='图书馆：私有成员',dining_hall='食堂：公有成员',science_hall='科学馆：保护成员'):
		#图书馆：私有成员，食堂：公有成员，科学馆：保护成员
		self.__library=library
		self.dining_hall=dining_hall
		self._science_hall=science_hall
		self.time=new_time
	def show(self):
		#输出None是因为没有返回值，所以不用print
		print(self.__library)

jnu=JNU()

#访问公有变量
print(jnu.dining_hall)

#访问私有变量
#print(jnu.__library)#不能用这种方式访问
print(jnu._JNU__library)#可以访问私有成员
jnu.show()

#访问保护变量
jnu._science_hall='可以修改科学馆的值'
#_下划线在IDLE表示最后一次正确执行的结果
print(jnu._science_hall)