for a in range(1, 1000):
    if all(((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0) for x in range(1, 1000)):
        print(a)