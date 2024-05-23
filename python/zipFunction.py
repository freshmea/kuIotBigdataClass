def main():
    alist = ['a1', 'a2', 'a3']
    blist = ['b1', 'b2', 'b3']
    for a, b in zip(alist, blist):
        print(a, b)
    kor_score = [45, 23, 53, 35, 93]
    math_score = [75, 53, 72, 65, 100]
    eng_score = [57, 38, 29, 69, 48]

    avarage = []
    for kor, math, eng in zip(kor_score, math_score, eng_score):
        print(f"kor {kor}, math {math}, eng {eng}")
        avarage.append((kor + math + eng) / 3)
    print(avarage)

if __name__ == '__main__':
    main()
