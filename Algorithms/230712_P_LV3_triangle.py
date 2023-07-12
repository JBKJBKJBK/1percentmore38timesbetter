def solution(triangle):
    answer = []
    # col = 0
    # suum = 0
    
    for idxR in range(len(triangle)):
        print(f'----idxR is {idxR} and r is {triangle[idxR]}----')
        if idxR == 0:
            answer.append(triangle[idxR])
            print(f'test1 {answer}')
            # print(f'test2 {triangle[idxR]}')
            print(f'test3 {answer[idxR]}')
            continue
        # print(f'test1 {answer}')
        # print(f'test2 {triangle[idxR]}')
        print(f'test3 {answer[idxR-1]}')

        # triangle[idxR] = [3, 8]
        newRow = []
        
        temp1, temp2 = 0, 0
        for idxC in range(len(answer[idxR-1])): 
            print(f'temps {temp1}, {temp2}')
            print(f'idx {idxR}, {idxC}')
            # print(f'----idxC is {idxC} and col is {triangle[idxR][idxC]}----')
            # print(f'out of range??? {answer[idxR-1][0]}')
            temp1 = answer[idxR-1][idxC] + triangle[idxR][idxC]
            if idxC == 0:
                newRow.append(temp1)
            elif temp1 > temp2:
                newRow.pop()
                newRow.append(temp1)
            temp2 = answer[idxR-1][idxC] + triangle[idxR][idxC+1]
            newRow.append(temp2)
            print(f'newRow is {newRow}')

        answer.append(newRow)
        print(f'--------answer is {answer}--------')
        
    return max(answer[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))