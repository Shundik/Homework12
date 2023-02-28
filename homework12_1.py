def test(x, y=10):
    e = 1
    i = 0
    while i < x:
        if i == 0:
            yield e
        else:
            e = e * y
            yield e
        i += 1


for n in test(20, 2):
    print(n)
