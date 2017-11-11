DIVISOR_DATA = {1: 0, 2: 1}

def special_divisor(n):
	if n in DIVISOR_DATA:
		return DIVISOR_DATA[n]
	if n % 2 == 0:
		DIVISOR_DATA[n] = special_divisor(n / 2) + 1
	else:
		DIVISOR_DATA[n] = min(special_divisor((n + 1) / 2) + 2, special_divisor((n - 1) / 2) + 2)
	return DIVISOR_DATA[n]


def answer(n):
	n = int(n)
	data = {1: 0, 2: 1}
	return special_divisor(n)