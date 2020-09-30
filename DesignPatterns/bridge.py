class DrawingApi1(object):
	def draw_circle(self, x, y, r):
		print(f"API 1 drawing circle at {x}, {y} with radius {r}")


class DrawingApi2(object):
	def draw_circle(self, x, y, r):
		print(f"API 2 drawing circle at {x}, {y} with radius {r}")


class Circle(object):
	def __init__(self, x, y, r, drawing_api):
		self._x = x
		self._y = y
		self._r = r
		self._drawing_api = drawing_api

	def draw(self):
		self._drawing_api.draw_circle(self._x, self._y, self._r)

	def scale(self, percent):
		self._r *= percent


circle1 = Circle(1, 2, 3, DrawingApi1())
circle2 = Circle(2, 3, 4, DrawingApi2())

circle1.draw()
circle2.draw()