from string import punctuation
not_in_id = punctuation.replace('-', '').replace('_', '').replace('.', '')
# print(not_in_id)

def firstStep(id):
    #1단계 : 대 -> 소
    return id.lower()

def secondStep(id):
    #2단계 : 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)
    for letter in id:
        if letter in not_in_id:
            id = id.replace(letter, '', )  
    return id

def thirdStep(id):
    #2번 이상 반복되는 . 제거
    for letter in id:
        print(letter)
        # if letter == '.':

    return

"""
def thirdStep(id):
    #2번 이상 반복되는 . 제거
    indexInfo = [0 if id[0] == '.' else None]
    for idx in range(1, len(id)):
        if id[idx-1] != '.' and id[idx] == '.':
            indexInfo.append(idx)
    print(indexInfo)
    return id
"""

"""
def thirdStep(id):
    #2번 이상 반복되는 . 제거
    prevletterisdot = False
    for i in range(len(id)):
        print(id[i])
        if prevletterisdot and id[i] == '.':
            print('check')
            id = id.replace(id[i], '', 1)    #replace 세번째인자 || string 문자 제거방법? list로 바꿔야하나
        if id[i] == '.':
            prevletterisdot = True
        else:
            prevletterisdot = False
        print(prevletterisdot, id)
    return id
"""

def fourthStep(id):
    #4단계 :마침표(.)가 처음이나 끝에 위치한다면 제거
    while id[0] == '.' or id[-1] == '.':
        if len(id) <= 1:
            return ''
        elif id[0] == '.':
            id = id[1:]
        elif id[-1] == '.':
            id = id[0:len(id)-1]
    return id

def fifthStep(id):
    #5단계 new_id가 빈 문자열
    if len(id) == 0:
        id += 'a'
    return id

def sixthStep(id):
    #길이 3~15자
    if len(id) >= 16:
        id = id[:15]
    while id[-1] == '.':
        id = id[0:len(id)-1]
    return id

def sevenStep(id):
    #길이 3~15자, 3자 미만일 시 마지막 문자반복
    letter = id[-1]
    # print(letter)
    while len(id) <= 2:
        id += letter
    return id



def solution(new_id):

    id = firstStep(new_id)
    # print('1: ', id)
    
    id = secondStep(id)
    # print('2: ', id)
    
    id = thirdStep(id)
    print('3: ', id)

    id = fourthStep(id)
    # print('4: ', id)

    id = fifthStep(id)
    # print('5: ', id)
        
    id = sixthStep(id)
    # print('6: ', id)

    id = sevenStep(id)
    # print('7: ', id)

    return id

id1 = "...!@BaT#*..y.abcdefghijklm"
id2 = "z-+.^."
id3 = "=.="
id5 = "abcdefghijklmn.p"
print(solution(id1))
# print(solution(id2))
# print(solution(id3))
# print(solution(id5))
