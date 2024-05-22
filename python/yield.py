def yield_example():
    print("yiel 함수가 호출되었습니다.")
    yield "test1"
    print("첫번째 yield 지점 통과")
    yield "test2"
    print("두번째 yield 지점 통과")
    yield "test3"
    

def main():
    print("main 함수가 호출되었습니다.")
    yield_object = yield_example()
    next(yield_object)
    print("a 지점 통과")
    
    next(yield_object)
    print("b 지점 통과")
    
    print(next(yield_object))
    print("메인 함수가 종료됨.")
    
    for i in yield_example():
        print(i)

if __name__ == "__main__":
    main()
