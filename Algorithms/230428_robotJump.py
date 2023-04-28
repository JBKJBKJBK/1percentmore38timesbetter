def pow2(n):
    i = 1
    result = []
    while i*2 <= n:
        # print(i)
        result.append(i)
        i *= 2
    return sorted(result, reverse=True)

# N = 20
# print(pow2(N))
"""
def solution(n):
    # q, r = divmod(n,2)
    # print(f'q is {q} and r is {r}')
    print('check', n//2,)

    # 2의 거듭제곱이면 두배씩 순간이동만하면 됨
    print('pow2 : ', pow2(n))
    if n in [1, 2, 4, 8, 16]:
        return 1
    
    if n%2 == 0:
        print('now')
        return solution(n//2)
    
    add = 1
    print('add')

    return solution(n//2) + add
"""

def solution(n):
    pow = pow2(n)
    print(pow)
    ans = 0

    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2

    for num in pow:
        q, r = divmod(n, num)
        print(f'q is {q} and r is {r}')
        if r == 0:
            n = q
            break
        if num == 2 and r == 1:
            ans = 1
            n = q
            break

    print(ans , n)
    return solution(n) + ans

N = 5000
print(solution(N))
