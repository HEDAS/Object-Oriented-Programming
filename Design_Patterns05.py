class JNU(object):
	def info(self):
		print("暨南大学（Jinan University），简称“暨大”（JNU）")

jnu=JNU()
jnu.info()
print("jnu属于JNU类吗？",isinstance(jnu, JNU))
print("jnu属于int类吗？",isinstance(jnu, int))
