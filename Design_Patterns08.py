import types
class JNU(object):
	'''***这是个新的暨南大学类***'''

	time='7:30-22:00'
	def __init__(self,new_time='7:30-17:30',library='图书馆：私有成员',dining_hall='食堂：公有成员',science_hall='科学馆：保护成员'):
		#图书馆：私有成员，食堂：公有成员，科学馆：保护成员
		self.__library=library
		self.dining_hall=dining_hall
		self._science_hall=science_hall
		self.time=new_time
	def show(self):
		#输出None是因为没有返回值，所以不用print
		print(self.time)

jnu_tianhe=JNU()#新建一个天河暨南大学对象
jnu_panyu=JNU()#新建一个番禺暨南大学对象
#self代表于对象自身，对比list.append()

JNU.network='Ruijie'#动态增加数据成员
print('暨南大学正常开放时间是？',jnu_panyu.time)
print('暨南大学的网络系统是？',jnu_panyu.network)

def military_training(self,need):#动态增加成员方法
	self.military_training_need=need 
jnu_tianhe.military_training=types.MethodType(military_training,jnu_tianhe)
jnu_tianhe.military_training(False)
print('暨南大学有没有军训？',jnu_tianhe.military_training_need)

#访问私有成员
jnu_tianhe.show()
JNU.time='7:30-12:00'
#试下修改show方法的print
#print(JNU.time)
jnu_panyu.show()
