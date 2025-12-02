class SafeCounter:
	def __init__(self,start=0):
		if not isinstance(start, int):
			raise TypeError("start must be int")
		self.value=start
	def inc (self, step=1):
		if step < 0:
			raise ValueError("step must be non-negative")
		self.value+=step
		return self.value
	def dec(self, step=1):
		if step < 0:
			raise ValueError("step must be non-negative")
		self.value-=step
		return self.value
	def reset(self):
		self.value = 0
	def __repr__(self):
		return f"SafeCounter (value={self.value})"
if __name__ == "__main__":
	c = SafeCounter(start=5)
	print("Start")
	c
	c.inc(3); print(repr(c))
	c.dec(2); print(repr(c))
	c.reset()
	print(repr(c))
	c
