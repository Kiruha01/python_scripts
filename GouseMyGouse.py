import winsound
noting = {'c4': 261, 'd4': 293, 'e4': 329, 'f4': 349,
		'g4': 391, 'a4': 440, 'b4': 493,}

def n(n, d=4):
	winsound.Beep(noting[n], 1000//d)
		
f = 'f4'
c = 'c4'
d = 'd4'
e = 'e4'
g = 'g4'
a = 'a4'
b = 'b4'
n(f)
n(e)
n(d)
n(c)
n(g, 2)
n(g, 2)

n(f)
n(e)
n(d)
n(c)
n(g, 2)
n(g, 2)

n(f)
n(a)
n(a)
n(f)
n(e)
n(g)
n(g)
n(e)
n(d)
n(e)
n(f)
n(d)
n(c, 2)
n(c, 2)
n(f)
n(a)
n(a)
n(f)
n(e)
n(g)
n(g)
n(e)
n(d)
n(e)
n(f)
n(d)
n(c, 2)
n(c, 2)
