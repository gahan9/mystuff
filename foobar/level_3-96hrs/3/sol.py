class Calculate(object):
	def __init__(self, **kwargs):
		self.useful_data = {1: 0, 2: 1}
		self.number = kwargs['number']

	def special_divisor(self, number):
		if number in self.useful_data:
			return self.useful_data[number]
		if number % 2 == 0:
			self.useful_data[number] = self.special_divisor(number / 2) + 1
		else:
			self.useful_data[number] = min(self.special_divisor((number + 1) / 2) + 2, self.special_divisor((number - 1) / 2) + 2)
		return self.useful_data[number]


def answer(n):
	result = Calculate(number=int(n))
	return result.special_divisor(int(n))

print(answer(15))
print(answer(16))
print(answer(155))
print(answer(70000))
print(answer('1565646546546545646546546546546546546546545646546546546546546545646489654165284518946528456'))
