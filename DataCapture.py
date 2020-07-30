def is_positive_int(func):

	def wrapper(*args):

		good = True

		for arg in args[1:]:
			if not isinstance(arg, int):
				print('❌ ({}) of type {} not added to collection, please pass a positive int'.format(arg,type(arg)))
				good = False
			else:
				if arg < 0:
					print('❌ ({}) is negative and not added to collection, please pass a positive int'.format(arg,type(arg)))
					good = False
					
		if good: 
			return func(*args)
		else:
			return ''

	return wrapper



class DataCapture:

	def __init__(self):

		"""
		* The constructor basically creates an empty list and an empty dictionary
		* The empty list is used to store added integers usind add method
		* The dictionary is used for build_stats method
		"""

		self.lst = []
		self.dct = {}

	
	@is_positive_int
	def add(self, n):

		"""
		* The decorator will verify if n is a positive integer.
		* If you pass a negative integer, the decorator will skip it and prints a message.
		* If you pass other data types, the decorator will also skip it and prints a message.
		* If no decorator issues found, the method append it to self.lst.
		"""
		self.lst.append(int(n))
		print('{} added'.format(n))


	def build_stats(self):

		"""
		* The method first checks if any integers were added.
		* If not, it will return an error message.
		* Otherwise, it will create a dictionary of intger:{'less':[],'greater':[]} items.
		* The values of 'less' and 'greater' are created using the filter iterators.
		"""

		if len(self.lst) == 0:
			print('❌ cannot find positive integers in collection, please add some first to build stats')

		else:
			for n in self.lst:
				less = [*filter(lambda i: i < n, self.lst)]
				greater = [*filter(lambda i: i > n, self.lst)]
				self.dct[n] = {'less':less, 'greater':greater}

	
	@is_positive_int
	def less(self, n):

		"""
		* The decorator will verify if n is a positive integer.
		* If you pass a negative integer, the decorator will skip it and prints a message.
		* If you pass other data types, the decorator will also skip it and prints a message.
		* If no decorator issues found,the method will checks if build_stats generated self.dct or not.
		* If yes, the method will check if n is already in dictionary.
		* If yes, the method will return the length of self.dct[n]['less']
		"""

		if len(self.dct) == 0:
			return '❌ cannot run less method before running build_stats method'

		else:
			if n in self.dct:
				return len(self.dct[n]['less'])
			else:
				return '❌ integer {} was not added to collection'


	@is_positive_int
	def greater(self, n):

		"""
		* The decorator will verify if n is a positive integer.
		* If you pass a negative integer, the decorator will skip it and prints a message.
		* If you pass other data types, the decorator will also skip it and prints a message.
		* If no decorator issues found, the method will checks if build_stats generated self.dct or not.
		* If yes, the method will check if n is already in dictionary.
		* If yes, the method will return the length of self.dct[n]['greater']
		"""

		if len(self.dct) == 0:
			return '❌ cannot run greater method before running build_stats method'

		else:
			if n in self.dct:
				return len(self.dct[n]['greater'])
			else:
				return '❌ integer {} was not added to collection'


	@is_positive_int
	def between(self, n, m):

		"""
		* The decorator will verify if n and m are positive integers.
		* If you pass a negative integer, the decorator will skip it and prints a message.
		* If you pass other data types, the decorator will also skip it and prints a message.
		* If no decorator issues found, the method will checks if n (start) is bigger than m (stop).
		* If yes, it will return an error.
		* If no, it will return the lengh of a listed filter iterator.
		"""

		if m not in self.lst:
			return '❌ param m {} is not found in collection!'.format(m)
		elif n not in self.lst:
			return '❌ param m {} is not found in collection!'.format(n)
		elif m < n:
			return '❌ param m {} is less than param n {}!'.format(m,n)
		else:
			return len([*filter(lambda x: m >= x >= n, self.lst)])

