# 1.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:    # 제곱수는 약수의 개수가 홀수
            answer -= i
        else:
            answer += i
    return answer



# 2. (위의 코드 한줄화)
def solution(left, right):
    return sum([-n if int(n ** 0.5) == n ** 0.5 else n for n in range(left, right+1)])





