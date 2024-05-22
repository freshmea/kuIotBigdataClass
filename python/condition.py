def min():
    # myage = int(input("나이를 넣으시오: "))
    # if  (myage > 30) and (myage < 50):
    #     print("클럽에 가입 되었습니다.")
    # else:
    #     print("아니요 클럽에 들어 올 수 없습니다.")

    score = int(input("점수를 넣으시오: "))
    if score >=90:
        grade = 'A'
    elif score >=80:
        grade = 'B'
    elif score >=70:
        grade = 'C'
    elif score >=60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"학점은 {grade} 입니다.")

    if True:
        print("참입니다.")
    if False:
        print("거짓입니다.")
    if 2:
        print("참입니다.")
    if 0:
        print("거짓입니다.")
    if 0.0:
        print("거짓입니다.")
    if 0.0001:
        print("참입니다.")
    if "":
        print("거짓입니다.")
    if "abc":
        print("참입니다.")
    if None:
        print("거짓입니다.")
    if []:
        print("거짓입니다.")
    if [1,2,3]:
        print("참입니다.")
        
    # 삼항 연산자
    x = 5
    y = 3
    if x > y:
        print("x가 y보다 큽니다.")
    else:
        print("x가 y보다 작거나 같습니다.")
        
    print("x가 y보다 큽니다.") if x > y else print("x가 y보다 작거나 같습니다.")


if __name__ == "__main__":
    min()
