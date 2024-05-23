from collections import Counter, OrderedDict, defaultdict, deque, namedtuple


def main():
    # deque
    deque_list = deque()
    for i in range(5):
        deque_list.append(i)
    print(deque_list)
    deque_list.appendleft(10)
    print(deque_list)
    deque_list.rotate(2)
    print(deque_list)
    deque_list.pop()
    print(deque_list)
    deque_list.popleft()
    print(deque_list)

    # OrderedDict
    d = OrderedDict()
    d['x'] = 100
    d['y'] = 200
    d['z'] = 300
    d['l'] = 500
    
    for k, v in d.items():
        print(k, v)
    
    for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
        print(k, v)
        
    # defaultDict
    d = defaultdict(lambda: 0)
    print(d)
    print(d['first'])
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(d.items())

    # Counter
    text = list("gallahad")
    c = Counter(text)
    print(c)

    # namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(x=11, y=22)
    print(p)
    print(p.x, p.y)

if __name__ == '__main__':
    main()