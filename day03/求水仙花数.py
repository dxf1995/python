for a in range(100,1000):
    x = int(str(a)[0])
    y = int(str(a)[1])
    z = int(str(a)[2])
    if a == (x**3 + y **3 + z **3):
        print(a)