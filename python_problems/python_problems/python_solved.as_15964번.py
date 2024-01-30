# 한 줄에 여러 개의 값을 입력하는 방법
'''
num1,num2=map(int,input().split())
def oprt(a,b):
    if ((1<=a<=100000)and(1<=b<=100000)):
        res = (a + b) * (a - b)
        return res
    else: 
        print("범위오류")

print(oprt(num1,num2))
'''
def oprt(a, b):
    res = (a + b) * (a - b)
    return res

num1, num2 = map(int, input().split())

if 1 <= num1 <= 100000 and 1 <= num2 <= 100000:
    print(oprt(num1, num2))
else:
    print("범위 오류")
'''
올바른 범위의 값인지 판단하는 부분에 문제가 있었음
내가 작성한 식에서는 그것을 함수 안에서 판단하게 함 

>> 문제: 범위 벗어난 값이 함수에 전달된다면 
        계산결과가 올바르지 않을 수 있음 
        (이 부분에서 오버플로우가 발생한다는 것인듯)

    함수에 값을 전달할때는 정해진 범위의 값만 전달해야 
    오류가 생기지 않음!
'''