for a in range(1, 1000):
    if all((108 % a == 0) and ((x % a != 0) <= ((x % 42 == 0) <= (x % 68 != 0))) for x in range(1, 20000)):
        print(a)