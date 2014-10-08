import random

class Reservoir():

	def __init__(self):
		__init__(self,1)
		return

	def __init__(self,N):
		self.sample_size=N
		self.data_size=0
		self.buffer=[]

	def add(self,item):
		self.data_size+=1
		if self.data_size>self.sample_size:
			
			if random.random()>(float(self.sample_size)/self.data_size):
				return
			else:
				pos=random.randint(0,self.sample_size-1)
				self.buffer[pos]=item
		else:
			self.buffer.append(item)
			

	def get(self):
		return self.buffer
