
def add(x, y):
    return x + y


print(add(2,3))
print(add('some  line', '**'))

def arg(x, y, z=100):
    return x * y * z


print(arg(1, 2))
print(arg(1, 2, 0.1))

def f_el_tup(a=(3,2,1)):
    return a[0];


print(f_el_tup((11,10,9)))
print(f_el_tup())

def s_of_circle(r):
    pi = 3.14159
    return r * pi**2


print(s_of_circle(1))
