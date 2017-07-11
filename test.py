
class TestClass:

	def __init__(self):
		self.version = 1

	def setVersion(self):
		try:
			self.version = self.version + 1
		except NameError:
			self.version = 1

	def printVersion(self):
		print self.version

tc = TestClass()
tc.setVersion()
tc.printVersion()

