def even_integer_function(n):
	for i in range(n):
		if i % 2 == 0:
			yield i

print(even_integer_function(10))

even_integers = (n for n in range(10) if n%2 == 0)
print(list(even_integers))

def fibonacci_gen():
	trailing, lead = 0, 1
	while True:
		yield lead
		trailing, lead = lead, trailing + lead

fib = fibonacci_gen()

from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
	try:
		obj.some_property += 1
		yield
	finally:
		obj.some_property -= 1

class Some_obj(object):
	def __init__(self, arg):
		self.some_property = arg

obj = Some_obj(5)
obj.some_property

with simple_context_manager(obj):
	print(obj.some_property)

def coroutine_example():
	while True:
		x = yield
		print(x)

c = coroutine_example()
#c.send(10)
c.next()
c.send(10)