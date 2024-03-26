import glob
import sys, os

directory = os.path.dirname(os.path.abspath(__file__)) + "/"

# 디렉토리 내의 모든 .txt 파일을 대상으로 합니다.
for filename in glob.glob(directory + "*.cpp"):
    # EUC-KR 인코딩으로 파일을 엽니다.
    content = ""
    print(filename)
    try:
        with open(filename, "r") as file:
            content = file.read()
        # UTF-8 인코딩으로 파일을 다시 저장합니다.
        with open(filename, "w", encoding="utf_8") as file:
            file.write(content)
    except Exception as e:
        print(e)
        continue
