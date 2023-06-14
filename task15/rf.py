for a in range(1, 1000):
    if all(not ((x * y> a) and (x > y) and (x < 8)) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)