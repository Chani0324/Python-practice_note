### 함수의 기본값 설정
from calendar import c


def profile(name, age=25, main_lang="파이썬"):
    print(f"이름 : {name}, 나이 : {age}, 언어 : {main_lang} ") 

profile("유재석")
profile("조세호", age=30)

### 가변 인자
def profile(name, age, *lang):
    print(f"이름 : {name}, 나이 : {age}")
    for i in lang:
        print(i)

profile("박명수", 20, "파이썬", "자바", "C++")



### 파일 열고 닫기
with open("test.txt", "w", encoding="utf8") as test_file:
    test_file.write("테스트 중")

with open("test.txt", "r", encoding="utf8") as test_file:
    print(test_file.read())


### Class
class Big_Sample:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Small_Sample(self):
        print(self.a * self.b + self.c)
        return self.a * self.b + self.c

k = Big_Sample(2, 3, 4).Small_Sample()
print(k)