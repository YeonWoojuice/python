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