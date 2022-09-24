
import e

# Ingestion

a = {
	'n': ['f', 'w', 'r', 'h', 'p', 'm', 'x', 'e', 't'],
	'x': [ 11,   2,   3,  66,   7,   2,   1,   5,   5],
	'y': [  0,   4,   0,   4,   7,   8,   9,   5,   5],
	'z': [ 22,   2,   7,  25,   7,   0,   6,   6,   3]
	}

x = e.DF(a)

print(x)

# Select

x = e.DF(a)

x.s(['x', 'z'])

print(x)

# Filter

x = e.DF(a)

x.f(x.y == 4)

print(x)

# Join

x = e.DF(a)

b = {
	'n': ['f', 'w', 'r', 'h', 'p'],
	'i': [65, 8, 1,  1, 9],
	'j': [ 8, 1, 4, 25, 1]
	}

y = e.DF(b)

x.j('n', 'n', y, 'i')

print(x)

# Append

x = e.DF(a)

c = {
	'x': [ 9, 1, 5, 29, 7],
	'z': [ 5, 9, 1,  5, 9],
	'k': [13, 9, 4, 11, 2]
}

z = e.DF(c)

x.a(c)

print(x)

# Extend

x = e.DF(a)

d = [1, 2, 3, 7, 8, 9, 13, 14, 15]

x.e('yo', 'i', d)

print(x)

# Map

x = e.DF(a)

x.m('m', lambda row: row.x + row.z - row.y)

print(x)

# Reduce

f = {
	'n': ['a', 'b', 'c'],
	'm': ['u', 'v', 'w'],
	's': [ 30,  20,  50],
	't': [  3,   7,  99]
}

g = e.DF(f)

g.r(sum, 'n', 's')

print(g)

# Pivot

x = e.DF(a)

x.p()

print(x)

# Unpivot

x = e.DF(a)

x.u()

print(x)