import string

# string
alphabet = string.ascii_uppercase
initial_dictionary = {}
for i in range(len(alphabet)):
    initial_dictionary[i+1] = alphabet[i]
# print(initial_dictionary)

def Add_Dict(dict, newWord):
    length = len(dict)
    dict[length+1] = newWord
    return dict

def Check_Dict(word, dict_values):
    if word in dict_values:
        return True
    return False

def solution(msg):
    dictionary = initial_dictionary
    values = list(dictionary.values())    # 형 변환 필요
    # print(values, type(values))
    answer = []

    for i in range(len(msg)-1):                         #마지막 알파벳 한 글자는 초기 dict에 포함
        curr_word = msg[i]
        next_letter = msg[i+1]
        # print(Check_Dict(curr_word, values))
        idx = i                                         # current : i, next : i+1 (초기)
        while Check_Dict(curr_word, values):            #value에 현재 선택 문자 있을 시,
            answer.append(values.index(curr_word)+1) 
            print('1: ', curr_word, next_letter) #현재 문자 인덱스 출력 , +1 주의

            if idx >= len(msg)-2:
                print(idx, 'break')
                break
            curr_word += next_letter                    #현재 + 다음
            next_letter = msg[idx+2]                      #다음 문자 준비
            print('2: ', curr_word, next_letter)

            print(Check_Dict(curr_word, values))
            idx += 1
        print('while 반복 끝')
        Add_Dict(dictionary, curr_word)

    return dictionary, answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))