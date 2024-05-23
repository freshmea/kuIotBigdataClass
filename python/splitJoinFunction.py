from matplotlib import colors


def main():
    # split
    items = 'zero one two three'.split()
    print(items)
    example = 'python,jquery,javascript,rust,go,cpp'.split(',')
    print(example)
    
    #join
    colors = ['red', 'blue', 'green', 'yellow']
    result = ''.join(colors)
    print(result)
    result2 = ', '.join(colors)
    print(result2)
    

if __name__ == '__main__':
    main()