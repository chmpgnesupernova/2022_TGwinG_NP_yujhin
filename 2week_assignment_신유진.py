# 문제 1번
def sum(a,b):
    return a+b

# 문제 2번
def sub(a,b):
    return a-b

# 문제 3번
def mul(a,b):
    return a*b

# 문제 4번
def div(a,b):
   return a/b

# 문제 5번
def distance(x1,y1,x2,y2):
    return pow((x1-x2)**2+(y1-y2)**2,1/2)

# 문제 6번
def short():
    lylic = "life is short art is long"
    a=lylic.split(' ')
    print(a[2])
short()

# 문제 7번
def myReverse(string):
    reverse=string[::-1]
    print(reverse)
    return reverse
string=input()

# 문제 8번
def letMeIntroduceMyself():
    a=input("이름:")
    b=input("취미:")
    c=input("학교:")
    d=input("생일:")
    say="""제이름은 {0}입니다. 취미는 {1}입니다.
           저는 {2}에 재학중이며 생일은 {3}입니다.""".format(a,b,c,d)
    print(say)
letMeIntroduceMyself()

# 문제 9번
def calcAI():
    a=int(input("첫번째 숫자를 입력하세요:"))
    b=int(input("두번째 숫자를 입력하세요:"))
    print("계산은 다음과 같습니다:",a+b)
calcAI()
