def sameLetter(prev, curr):
    if prev[-1] == curr[0]:
        return True
    return False

def solution(n, words):
    already = []
    for i in range(len(words)):
        # 몫(q) + 1 : 몇바퀴째 게임
        # 나머지(r) + 1 : 몇번째 사람 차례
        q, r = divmod(i, n)
        # print(f'q is {q}, r is {r}')
        
        # 단어 길이가 한 글자이면 탈락
        if len(words[i]) == 1:
            return [r+1, q+1]
        
        # checkLetter : 앞단어 뒷글자 vs. 현재단어 앞글자 
        # checkAlready : 이미 말한 단어인지
        checkLetter = not(sameLetter(words[i-1], words[i]))
        checkAlready = words[i] in already
        
        # 이미 말한 단어 더해주고, 첫번째 단어면 일단 패스
        already.append(words[i])
        if i == 0:
            continue
        # print('check1', already)
        # print('word : ', words[i])
        
        # 틀리면 그 때 게임바퀴 수, 차례인 사람 반환
        # print(checkAlready, checkLetter)
        if checkAlready or checkLetter:
            return [r+1, q+1]

    return [0,0]