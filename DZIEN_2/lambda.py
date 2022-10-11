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
