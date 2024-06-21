def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for f in fib():
    if f > 100:
        break
    print(f)


def sqd():
    i = 1
    while True:
        yield i*i
        i += 1

for n in sqd():
    if n > 100:
        break
    print(n)

def cube():
    i = 1
    while True:
        yield i*i*i
        i += 1

for c in cube():
    if c >1000:
        break
    print(c)