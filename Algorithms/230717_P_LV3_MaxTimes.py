def solution(n, s):
    return

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
print(solution(n, s))