def solution(n, s):
    if int(s/n) == 0:
        return [-1]
    
    # answer = [int(s/n)+1 for i in range(n)]
    standard = int(s/n)+1
    check = standard * n
    # print(f'standard {standard} and check {check}')
    
    while True:
        # print(check)
        diff = check - s
        if check == s:
            break
        elif check > s:
            answer = [standard-1 for i in range(diff)] + [standard for i in range(n-diff)]
        # print(f'{i}th answer is {answer}')
        check = sum(answer)

    return answer

""" 2차시도 효율성
def solution(n, s):
    if int(s/n) == 0:
        return [-1]

    answer = [int(s/n)+1 for i in range(n)]
    i = 0
    while sum(answer) != s:
        answer[i] -= 1
        # print(f'{i}th answer is {answer}')
        i += 1

    return answer
"""

""" 1차시도 런타임 에러
def solution(n, s):
    if n == 1:
        return [s]
    
    answer = []
    standard = int(s/n)
    print(f'standard is {standard}')
    if standard == 0:
        return [-1]
    
# while True:
#     if abs(s-standard) < n:
#         answer.append(s)
#         break
    temp = int(s/n)
    print(f'temp is {temp}')
    answer.append(temp)
    s -= temp
    print(f'now s get changed to {s}')
    recurr = solution(n-1, s)
    print(f'recurrsive list {recurr}')
    
    return answer + recurr
"""

n, s = 2, 9
n, s = 3, 8
print(solution(n, s))