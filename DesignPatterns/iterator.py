def count_to(count):
	num_in_french = ['un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix']

	iterator = zip(range(count), num_in_french)

	for position, number in iterator:
		yield number


for num in count_to(10):
	print(f"{num}")