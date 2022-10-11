print((lambda s:f"to jest wynik lambda: {s}")("zgnieżdzenie w funkcji print"))

def msg(s):
    return f"to jest wynik zwykłej funkcji: {s}"

print(msg("zwykła funkcja"))

print((lambda x:x*3)(4))

def policz(x):
    return x*3

print(policz(4))

x = lambda a:a+555

print(x(6))

y = lambda a,b,c=2:(a-b)*c
print(y(1,4,7))
print(y(1,4))

def multi(n):
    return lambda a:a*n

d = multi(56)
print(d(7))

print(multi(34)(19))

liczby = [3,13,-1,0,4,15,16,22,23,101,99,120,-900,40,45]
