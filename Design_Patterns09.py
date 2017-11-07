class JNU(object):
	'''***这是个新的暨南大学类***'''

	total=0
	def __new__(cls,*args,**kwargs):
		if cls.total >= 5:
			raise Exception('最多只能建立5间学校')
		else:
			JNU.total+=1
			return object.__new__(cls)

jnu_tianhe=JNU()
jnu_panyu=JNU()
jnu_zhuhai=JNU()
jnu_shenzhen=JNU()
jnu_huawen=JNU()
#jun_USA=JNU()