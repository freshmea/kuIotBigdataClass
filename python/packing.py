def min():
    t = [1, 2, 3]
    a, b, c = t
    print(t, a, b, c)
    print(t, *t)

    t2= (4, 5, 6)
    d, e, f = t2
    (d, e, f) = t2
    print(t2, d, e, f)

if __name__ == "__main__":
    min()
