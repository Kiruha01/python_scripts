import pyautogui as pg
import math

DOWN = True




if DOWN:
	def mouseDown():
		pg.mouseDown(button='left')
else:
	def mouseDown():
		pass

class Point(object):
	"""docstring for point"""
	def __init__(self,x=0, y=0, c=None, prst=False):
		self.x = x
		self.y = y
		self.unpress = prst
		if c:
			self.x = c.x
			self.y = c.y
	def change_coord(self, x, y):
		self.x += x
		self.y += y

def click(pos):
	pg.moveTo(pos)
	mouseDown()
	pg.mouseUp()



# def half_round(center, r, start, end, part='up', step=10):
# 	#    <-start-|--end-->
# 	#	|                |
# 	#	 \              / 
# 	#	   -------------

# 	#
# 	if abs(start) > r:
# 		start = r * (abs(start)//start)
# 	if abs(end) > r:
# 		end = r * (abs(end)//end)
# 	# Защита от start/end > r

# 	if (-start > end):
# 		step *= -1
# 	# Рисовать в нужную сторону
# 	if part == 'up':
# 		pg.moveTo(center.x - start, center.y - math.sqrt(r**2 - start**2))
# 		mouseDown()
# 		for i in range(-start, end, step):
# 			pg.moveTo(center.x + i, center.y - math.sqrt(r**2 - i**2))
# 		pg.moveTo(center.x + end, center.y - math.sqrt(r**2 - end**2))
# 		pg.mouseUp()
# 	elif part == 'dn':
# 		pg.moveTo(center.x - start, center.y + math.sqrt(r**2 - start**2))
# 		mouseDown()
# 		for i in range(-start, end, step):
# 			pg.moveTo(center.x + i, center.y + math.sqrt(r**2 - i**2))
# 		pg.moveTo(center.x + end, center.y + math.sqrt(r**2 - end**2))
# 		pg.mouseUp()

def half_round(center, r, x0, x1, part='up'):
	if abs(x0) > r:
		x0 = r * (abs(x0)//x0)
	if abs(x1) > r:
		x1 = r * (abs(x1)//x1)

	dfi = 2*math.pi / 30
	if (-x0 > x1):
		dfi *= -1
	if part == 'dn':
		prt = 1
	else:
		prt = -1
	b = math.acos(x1 / r)
	fi = math.acos(x0 / r)
	x = center.x
	y = center.y
	pg.moveTo(x-x0, y + r*math.sin(fi)*prt)
	pg.mouseDown()
	while ((fi+dfi + b <= math.pi) and (dfi > 0)) or ((fi+dfi + b >= math.pi) and (dfi < 0)):
		pg.moveTo(x - r*math.cos(fi), y + r*math.sin(fi)*prt)
		fi += dfi
	pg.moveTo(x - r*math.cos(math.pi - b), y + r*math.sin(math.pi - b)*prt)
	pg.mouseUp()

def draw_heart(center, r):
	# input('красный')
	# red = pg.position()
	# input('заливка')
	# z = pg.position()
	l = Point(center.x - 2*r, center.y)
	ra = Point(center.x + 2*r, center.y)
	sl = Point(center.x - r, center.y)
	sr = Point(center.x + r, center.y)

	half_round(sl, r, r, r)
	half_round(ra, 4*r, 2*r, -4*r, 'dn')
	half_round(l, 4*r, -2*r, 4*r, 'dn')
	half_round(sr, r, -r, -r)

	# click(red)
	# click(z)
	# pg.moveTo(center.x, center.y + 10)
	# pg.mouseDown()
	# pg.mouseUp()

def line_to(x, y):
	pg.moveTo(x, y)

def OLDline_to(x, y):
	pg.mouseDown()
	pg.moveTo(x, y)
	pg.mouseUp()


def round(center, r, onClock=True):
	if onClock:
		half_round(center, r, r, r, 'up')
		half_round(center, r, -r, -r, 'dn')
	else:
		half_round(center, r, -r, -r, 'up')
		half_round(center, r, r, r, 'dn')

def draw_poligon(points):
	for pnt in points:
		# if pnt.unpress:
		# 	pg.mouseUp()
		# else:
		# 	pg.mouseDown()
		line_to(pnt.x, pnt.y)


def draw_dick(start, r, l, n):
	"""
	r - диаметр яиц
	l - длина члена
	n - ширина члена
	start - объект 'point' с координатами центра левого яйца

	"""
	center_l = Point(c=start)
	center_r = Point(start.x + n, start.y)

	half_round(center_l, r, 0, -r)
	half_round(center_l, r, r, n//2, 'dn')

	half_round(center_r, r, n//2, r, 'dn')
	half_round(center_r, r, -r, 0)

	if n > 2*r:
		m = n//2
		x1 = (m**2 - r**2 - (m-r)**2)/(2*r)
		r1 = math.sqrt(x1**2 + m**2)
		t = Point(start.x + n//2, start.y - x1 - r)
		half_round(t, r1, n//2 - r, n//2 - r, 'dn')


	pg.moveTo(start.x, start.y - r)
	OLDline_to(start.x, start.y - r - l)

	pg.moveTo(start.x + n, start.y - r)
	OLDline_to(start.x + n, start.y - r - l)


	center_g = Point(start.x + n//2, start.y - l - r)
	half_round(center_g, n//2, n//2, n//2)

	center_pipki = Point(center_g.x, center_g.y - n//2)
	r_pip = n/math.sqrt(2)

	half_round(center_pipki, r_pip, n//2, n//2, 'dn')
	pg.moveTo(center_pipki.x, center_pipki.y)
	OLDline_to(center_pipki.x, center_pipki.y + n//4)


def П(point, k):
	x = point.x
	y = point.y
	pg.mouseDown()
	line_to(x+k, y)
	line_to(x+k, y-3.5*k)
	line_to(x+2*k, y - 3.5*k)
	line_to(x+2*k, y)
	line_to(x+3*k, y)
	line_to(x+3*k, y - 4.5*k)
	line_to(x, y - 4.5*k)
	line_to(x,y)
	pg.mouseUp()
	pg.moveTo(x+4*k, y)


def М(point, k):
	x = point.x
	y = point.y
	pg.mouseDown()
	line_to(x+k, y)
	line_to(x+k, y-3*k)
	line_to(x+1.5*k, y-2*k)
	line_to(x+2*k, y-3*k)
	line_to(x+2*k, y)
	line_to(x+3*k, y)
	line_to(x+3*k, y-4.5*k)
	line_to(x+2*k, y-4.5*k)
	line_to(x+1.5*k, y-3.5*k)
	line_to(x+k, y-4.5*k)
	line_to(x, y-4.5*k)
	line_to(x, y)
	pg.mouseUp()
	pg.moveTo(x+4.5*k, y)

def defis(point, k):
	x = point.x
	y = point.y-2*k
	pg.moveTo(x, y)
	pg.mouseDown()
	line_to(x+1.5*k, y)
	line_to(x+1.5*k, y-0.5*k)
	line_to(x, y-0.5*k)
	line_to(x, y)
	pg.mouseUp()
	pg.moveTo(x+2*k, y+2*k)

def У(point, k):
	x = point.x
	y = point.y
	center1 = Point(x+1.5*k, y-1.5*k)
	half_round(center1, int(1.5*k), int(1.5*k), int(1.5*k), 'dn')
	y = point.y-1.5*k
	pg.mouseDown()
	line_to(x+3*k, y-3*k)
	line_to(x+2*k, y-3*k)
	line_to(x+2*k, y-1.5*k)
	line_to(x+1.5*k, y-1.5*k)
	center2 = Point(x+1.5*k, y-2*k)
	pg.mouseUp()
	half_round(center2, int(0.5*k), 0, -int(0.5*k), 'dn')
	pg.mouseDown()
	line_to(x+k, y-3*k)
	line_to(x, y-3*k)
	line_to(x, y-1.5*k)
	pg.mouseUp()
	center3 = Point(x+k, y-1.5*k)
	half_round(center3, int(k), k, 0, 'dn')
	pg.mouseDown()
	line_to(x+2*k, y-0.5*k)
	line_to(x+2*k, y)
	pg.mouseUp()
	half_round(center1, int(0.5*k), -int(0.5*k), -int(0.5*k), 'dn')
	pg.mouseDown()
	line_to(x,y)
	pg.mouseUp()

def circleOct(center, r, step=10):
	x1 = center.x
	y1 = center.y
	x = 0
	y = r
	delta = 1 - 2*r
	error = 0
	while(y >= 0):
		print(x, y)
		line_to(x1 + x, y1 + y)
		error = 2*(delta + y) - 1
		if ((delta < 0) and (error <= 0)):
			x += step
			delta += 2*x+1
			continue
		elif ((delta > 0) and (error > 0)):
			y -= step
			delta -= 2*y+1
			continue
		else:
			x += step
			delta += 2*(x-y)
			y -= step




def cirleLine(center, r, n):
	dfi = 2*math.pi / n
	fi = 0
	x = center.x
	y = center.y
	pg.moveTo(x+r, y)
	pg.mouseDown()
	for i in range(n+1):
		pg.moveTo(x + r*math.cos(fi), y + r*math.sin(fi))
		fi += dfi
	pg.mouseUp()


if __name__ == '__main__':
	a = input("h - heart; d - dick; p - PM-PU; other - round")
	if a == 'h':
		r = int(input('Диаметр шаров '))
		input('Enter чтобы начать')
		start = pg.position()
		draw_heart(start, r)
	elif a == 'd':
		r = int(input('Диаметр '))
		l = int(input('Длина '))
		n = int(input('Ширина '))
		start = pg.position()
		draw_dick(start, r,l,n)
	elif a == 'p':
		K = int(input("Коэффициент размера "))
		x,y = pg.position()
		start = Point(x,y)
		П(start, K)
		x,y = pg.position()
		start = Point(x,y)
		М(start, K)
		x,y = pg.position()
		start = Point(x,y)
		defis(start, K)
		x,y = pg.position()
		start = Point(x,y)
		Р(start, K)
		x,y = pg.position()
		start = Point(x,y)
		У(start, K)
	elif a == 'q':
		x,y = pg.position()
		start = Point(x,y)
		ll = [start,]
		ll.append(Point(x+10, y))
		ll.append(Point(x+5, y-30))
		ll.append(Point(x+30, y+20, True))
		ll.append(Point(x-60, y))
		mouseDown()
		draw_poligon(ll)
	else:
		f = pg.position()
		half_round(f, 100, 50, -80)
		half_round(f, 100, -60, -50)
		half_round(f, 100, -80, 30)

	# K = 50
	# x,y = pg.position()
	# start = Point(x,y)
	# P(start, K)
	# x,y = pg.position()
	# start = Point(x,y)
	# M(start, K)
	# x,y = pg.position()
	# start = Point(x,y)
	# defis(start, K)
	# x,y = pg.position()
	# start = Point(x,y)
	# P(start, K)
	# x,y = pg.position()
	# start = Point(x,y)
	# U(start, K)

	# x,y = pg.position()
	# cen = Point(x,y)
	# cirlehalf(cen, 100, 70, 50, 'up')
	# cirlehalf(cen, 100, 70, -100, 'up')
	# cirlehalf(cen, 100, -70, -50, 'dn')
	# cirlehalf(cen, 100, -100, -50, 'dn')


	# r1 = int(input())
	# center = pg.position()

	# r = r1
	# pg.moveTo(center.x-r, center.y)
	# pg.mouseDown(button='left')

	# for i in range(-r, r+1, 10):
	# 	x = center.x + i
	# 	y = center.y + math.sqrt(r**2 - i**2)
	# 	pg.moveTo(x,y)

	# for i in range(r, -r-1, -10):
	# 	x = center.x + i
	# 	y = center.y - math.sqrt(r**2 - i**2)
	# 	pg.moveTo(x,y)
	# pg.moveTo(center.x -r, center.y)
	# pg.mouseUp()
