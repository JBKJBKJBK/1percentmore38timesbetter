def solution(w,h):
    total = w * h
    
    if w == 1 or h == 1:
        return 0
    
    # 배수 약수 관계
    elif w%h == 0 or h%w == 0:
        return total - h
    
    # w, h 모두 짝수
    elif w%2 == 0 and h%2 == 0:
        w2, h2 = int(w/2), int(h/2)
        print(w2, h2)
        return 2*w2*h2 + 2*solution(w2, h2)
    
    else:
        linePassing = h + w -1
        # print(f'Line passes {linePassing}')
        return total - linePassing
    
w, h = 8, 9
w, h = 8, 8
print(solution(w, h))