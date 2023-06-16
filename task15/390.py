for a in range(1, 1000):
    if all((110 % a == 0) and(((x % 80 == 0) and (x % 75 == 0)) <= (x % a == 0)) for x in range(1, 20000)):
        print(a)