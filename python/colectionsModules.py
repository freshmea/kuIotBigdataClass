from collections import deque


def main():
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

if __name__ == '__main__':
    main()