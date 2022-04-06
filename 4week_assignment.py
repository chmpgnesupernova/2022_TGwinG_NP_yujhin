# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번


def intervention(queue):
    answer = list()
    if "성은" not in queue:
        queue.append("승호")
    else:
        num=queue.index("성은")
        if num<5:
            queue.append("승호")
        else:
            queue.insert(num+1,"승호")
    answer=queue
    return answer

# 문제 2번




# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    new=list()
    n=len(searchWords)
    for i in range(n):
        if entry in searchWords[i]:
            new.append(searchWords[i])
    new.sort()
    answer=new
    return answer


# 문제 4번
def stock_price(stockChart):
    answer = str()
    sum=[stockChart[0]]
    print(sum)
    i=0
    for i in range(len(stockChart)-1):
        sum.append(sum[i]+stockChart[i+1])
        print(sum)
    sum.reverse()
    print(sum)
    minimum=sum[0]
    for j in range(len(sum)-1):
        if minimum>sum[j+1]:
            minimum=sum[j+1]
            day=j+1
            print(day)
        elif minimum==sum[j+1]:
            day=j+1
            print(day)
        else:
            print(day)
    answer=day
    return answer


# 문제 5번
def decryption(letter):
    answer = str()
    translate=str()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    
    for i in range(len(letter)):
        
        for j in range(len(alphabet)):
            if alphabet[j]==letter[i]:
                translate=translate+alphabet[j-3]
        if letter[i] not in alphabet:
            translate=translate+letter[i]
   
    answer=translate
    return answer