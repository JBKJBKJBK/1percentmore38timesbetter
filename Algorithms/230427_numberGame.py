def solution(A, B):
    sortA = sorted(A, reverse = True)
    sortB = sorted(B, reverse = True)
    L = len(A)
    
    score = 0
    for b in sortB:
        for a in sortA:
            if b > a:
                score += 1
                sortA.remove(a)
                # print(f'sortA {sortA}')           
                break
    return score