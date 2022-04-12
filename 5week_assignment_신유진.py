# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점
from math import *
def calcCircleArea(r):
    result = float()
    val_CircleArea=round(r*r*pi,2)
    result=val_CircleArea
    return result

def calcLog(a, b):
    result = float()
    val_Log=round(log(b,a),2)
    result=val_Log
    return result

def calcSin(x):
    result = float()
    val_Sin=sin(x)
    result=round(val_Sin,2)
    return result

def calcFactorial(x):
    result = int()
    val_Factorial=round(factorial(x),2)
    result=val_Factorial
    return result

def calcCombination(n, r):
    result = int()
    val_Combination=round(comb(n,r),2)
    result=val_Combination
    return result

def calculator(order):
    answer = 0
    if "원넓이" in order:
        order_List=order.split()
        input_CircleArea=order_List[1]
        answer=calcCircleArea(float(input_CircleArea))
    elif "로그" in order:
        order_List=order.split()
        input_Log_Base=order_List[1]
        input_Log_X=order_List[2]
        if input_Log_Base=="e":
            answer=calcLog(e,float(input_Log_X))
        else:
            answer=calcLog(float(input_Log_Base),float(input_Log_X))
    elif "사인" in order:
        order_List=order.split()
        input_Sin=order_List[1]
        answer=calcSin(float(input_Sin))
    elif "팩토리얼" in order:
        order_List=order.split()
        input_Factorial=order_List[1]
        answer=calcFactorial(int(input_Factorial))
    elif "조합" in order:
        order_List=order.split()
        input_Combination_n=order_List[1]
        input_Combination_r=order_List[2]
        answer=calcCombination(int(input_Combination_n),int(input_Combination_r))
    return answer
