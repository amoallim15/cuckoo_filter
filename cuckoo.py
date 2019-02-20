

class cuckooBucket:
	def __init__(self, bucket_size):
		self.bucket_size = bucket_size
		self.bucket = []
		pass

	def __contain__(self, finger_print):
		pass
		
	def insert(self):
		pass

	def delete(self):
		pass

class cuckooFilter:
	def __init__(self, table_size, bucket_size, finger_print_size, hash_fns, max_swaps= 100):
		self.table_size = table_size
		self.bucket_size = bucket_size
		self.finger_print_size = finger_print_size
		self.hash_fns = hash_fns
		self.max_swaps = max_swaps
		self.table = []

		for i in range(self.table_size):
			self.table.append() # TODO: cuckooBucket
		pass

	def insert(self, value):
		pass

	def delete(self):
		pass

	def lookup(self):
		pass