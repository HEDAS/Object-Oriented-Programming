class Vehicle(object):
	"""docstring for Vehicle"""
	def __init__(self, type='Car', brand='Hong Qi'):
		self.setType(type)
		self.setBrand(brand)

	def setType(self,type):
		if type not in ('MotorBoat','Car','AirPlane','Bicycle'):
			print("type must be 'MotorBoat' or 'Car' or 'AirPlane' or 'Bicycle'")
			self.__type='Car'
			return
		self.__type=type

	def setBrand(self,brand):
		if brand not in ('Hong Qi','ofo'):
			print("brand must be 'Hong Qi' or 'ofo'")
			self.__brand='Hong Qi'
			return
		self.__brand=brand

	def show(self):
		print(self.__type,self.__brand,sep='\n')

#my_vehicle=Vehicle()
#my_vehicle.show()

class Car(Vehicle):
	"""docstring for Car"""
	def __init__(self, type='Car',brand='ofo',engine_system_include=True):
		super(Car, self).__init__(type,brand)
		self.setEngineSystem(engine_system_include)

	def setEngineSystem(self,engine_system_include):
		if not isinstance(engine_system_include, bool):
			print('engine system must be check')
			self.__engine_system_include=False
			return
		self.__engine_system_include=engine_system_include
	
	def show(self):
		super(Car,self).show()
		print(self.__engine_system_include)

if __name__ == '__main__':
	my_vehicle=Vehicle('Bicycle','ofo')
	my_vehicle.show()
	print("=============================")

	Jack_vehicle=Car('Car','Hong Qi',True)
	Jack_vehicle.show()
	print("=============================")

	MaYun_vehicle=Car()
	MaYun_vehicle.show()
	print("=============================")

#多态的实现主要通过重写基类的方法实现，比如改变show，注释掉super的show