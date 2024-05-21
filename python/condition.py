def min():
    myage = int(input("나이를 넣으시오: "))
    if  (myage > 30) and (myage < 50):
        print("클럽에 가입 되었습니다.")
    else:
        print("아니요 클럽에 들어 올 수 없습니다.")
    
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

if __name__ == "__main__":
    min()
