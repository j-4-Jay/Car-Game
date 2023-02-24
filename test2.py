class cabinet:

	def __init__(self, width, depth, height, qnt):
		self.width = width
		self.depth = depth
		self.height = height
		self.qnt = qnt

	def shlv_sft(self):
		return self.width * self.depth / 92903.04
	def partition_sft(self):
		return self.depth * self.height / 92903.04

cab1 = cabinet(600, 600, 800, 1)

print(round(cab1.shlv_sft()))

