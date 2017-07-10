a = 1
b = [1]
c = {}

print a
print b
print c

def change():
    a = 2
    b[0] = 2
    # c = {'hi':2}
    c['hi'] = 2

    print a
    print b
    print c

change()
