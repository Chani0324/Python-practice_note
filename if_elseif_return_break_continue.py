### if 여러개와 elseif를 사용하는 것의 차이
## if 하나와 elseif 여러개 : if, elseif 들의 여러 조건들 중 하나만 만족하면 해당 if, elseif문은 넘어감
## if 여러개 사용 : if 들의 여러 조건들을 하나씩 모두 비교함. 

### return, break, continue의 차이
## return : 해당 '함수'를 빠져나가면서 값을 반환해줌. a라는 변수에 return이 없는 함수를 적용시키면 print(a)시 none이 나오지만
##          return 사용 후 print(a)시 a에 반환되는 값이 출력 됨.
## break : 전체 반복문을 빠져나감
## continue : 특정 조건의 한 시점의 반복문을 빠져나가고 다음 반복문을 실행.

######################## 예제 ##############################

def test(x, y):
    while(True):
        if y > x :
            print("y가 x보다 큽니다.")
            print(x)
            return x
        elif x == 0:
            print("x 값이 0이 되었습니다.")
            break
        else:
            print(x)
            x -= y
            
        if x == 0:
            print("x 값이 0이 되었습니다.")
            
            
d = test(10, 1)
print(d)


###################################################



