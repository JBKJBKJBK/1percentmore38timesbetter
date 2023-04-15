n, t, m, p = 2, 4, 2, 1
# n, t, m, p = 16, 16, 2, 1
# n, t, m, p = 16, 16, 2, 2

def changeSys(nth, num):
    dict = {}
    values = "0123456789ABCDEF"
    for i in range(16):
        dict[i] = values[i]
    # print(dict)

    result = ""
    while True:
        q, r = divmod(num, nth)
        # print(q, r)
        num = q
        result = dict[r] + result
        if q == 0:
            break
        elif num < nth :
            result = dict[q] + result
            break
    return result

# print(changeSys(3, 11))
# print(changeSys(3, 1101))
# print(changeSys(16, 47))
# print(changeSys(16, 51))
# print(changeSys(16, 1))

def allAnswers(n, turns):
    answers = "0"
    for i in range(1, turns):
        if len(answers) > turns:
            break
        # print(n, i)
        temp = changeSys(n, i)
        # print('temp', temp, type(temp))
        answers += temp
    return answers

# print(allAnswers(n, t*m))

def solution(n, t, m, p):
    myAnswer = ""
    answers = allAnswers(n, t*m)
    # print('answers :', answers)
    for i in range(len(answers)-2):
        # 2, 4, 5, 11, 14 번
        if len(myAnswer) >= t:
            break
        if i%m == p-1 :
            # print(i, m, 'i%m = ', i%m)
            # print(answers[i])
            myAnswer += answers[i]
    return myAnswer

# ------------ 230415 ㅈㅐ구ㅣ호출 사용 ------------
# n : n 진법
def recurChangeSys(nth, num, dict):
    result = ""
    while True:
        q, r = divmod(num, nth)
        num = q
        result = dict[r] + result
        if q == 0:
            break
        elif num < nth :
            result = dict[q] + result
            break
    return result


def recursiveAllAnswers(n, i, length, turns, dict):
    print('start     ', n, i, length, turns, dict[10])
    temp = recurChangeSys(n, i, dict)
    print(temp)

    if length > turns:
        return ""
    return temp + recursiveAllAnswers(n, i+1, length+len(temp), turns, dict)

# print(recursiveAllAnswers(2, 0, 0, 10))

def recurSolution(n, t, m, p):
    dict = {}
    values = "0123456789ABCDEF"
    for i in range(16):
        dict[i] = values[i]

    myAnswer = ""
    answers = recursiveAllAnswers(n, 0, 0, t*m, dict)
    print('answers :', answers)
    for i in range(len(answers)-2):
        # 2, 4, 5, 11, 14 번
        if len(myAnswer) >= t:
            break
        if i%m == p-1 :
            # print(i, m, 'i%m = ', i%m)
            # print(answers[i])
            myAnswer += answers[i]
    return myAnswer

print(recurSolution(n, t, m, p))


