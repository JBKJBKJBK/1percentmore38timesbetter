def pow2(n):
    i = 1
    result = []
    while i*2 <= n:
        print(i)
        result.append(i)
        i *= 2
    return result

# N = 20
# print(pow2(N))

def solution(n):
    # q, r = divmod(n,2)
    # print(f'q is {q} and r is {r}')
    print('check', n//2)

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

N = 50
print(solution(N))