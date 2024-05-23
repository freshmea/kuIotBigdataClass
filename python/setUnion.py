def main():
    s = set({1,2,3,1,2,3})
    s1 = {1,2,3,1,2,3}
    print(s)
    print(s1)
    s.add(7)
    print(s)
    s.remove(1)
    print(s)
    s.update([11, 12, 13])
    s.update({14, 15, 16})
    print(s)
    # s.clear()
    # print(s)
    # s2 = s1.union(s)
    s2 = s1 | s
    # s3 = s1.intersection(s)
    s3 = s1 & s
    # s4 = s1.difference(s)
    # s5 = s.difference(s1)
    s4 = s1 - s
    s5 = s - s1
    print(f"s: {s}")
    print(f"s1: {s1}")
    print(f"합집합 s1, s: {s2}")
    print(f"교집합 s1, s: {s3}")
    print(f"차집합 s1 - s: {s4}")
    print(f"차집합 s - s1: {s5}")

if __name__ == '__main__':
    main()
