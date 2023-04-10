#  230410 재시도
import string
from tabnanny import check

# string
alphabet = string.ascii_uppercase
initial_dictionary = {}
for i in range(len(alphabet)):
    initial_dictionary[i+1] = alphabet[i]
# print(initial_dictionary)

def Check_Dict(word, dict_values):
    # dict_values = dict.values()
    if word in dict_values:
        return True
    return False

def Add_Dict(dict, newWord):
    values = list(dict.values())
    if not Check_Dict(newWord, values):
        length = len(dict)
        dict[length+1] = newWord
    return dict


# def solution(msg):
#     dictionary = initial_dictionary
#     values = list(dictionary.values())    # 형 변환 필요
#     # print(values, type(values))
#     answer = []

#     for i in range(len(msg)-1):
#         curr_word = msg[i]
#         next_letter = msg[i+1]
#         # print(Check_Dict(curr_word, values))
    
#         while Check_Dict(curr_word, values):            #value에 현재 선택 문자 있을 시,
#             answer.append(values.index(curr_word)+1)    #현재 문자 인덱스 출력 , +1 주의
#             curr_word += next_letter                    #현재 + 다음
#             # print(curr_word)
#             print('index : ', values.index(next_letter)+1)
#             next_letter = msg[values.index(next_letter)+1]    #다음 문자 준비
#             print('curr : ', curr_word, 'next : ', next_letter)
#             print('더할 문자: ', curr_word, next_letter)
#             print(Check_Dict(curr_word, values))
#         Add_Dict(dictionary, curr_word)

#     return dictionary, answer

# 230410
def solution(msg):
    dictionary = initial_dictionary
    values = list(dictionary.values())    # 형 변환 필요
    answer = []

    i = 0
    while i <= len(msg)-2:
        # print('=================')
        curr_word = msg[i]
        next_letter = msg[i+1]
        check_word = curr_word+next_letter
        # print('i = ', i)
        # print('test1 : ', curr_word, next_letter)
        # print('check1 : ', check_word)

        while Check_Dict(check_word, values):
            # print('Yes, there is.')
            curr_word += next_letter
            i += 1
            if i > len(msg)-2:
                # print('break')
                break
            next_letter = msg[i+1]
            check_word = curr_word+next_letter
            # print('test2 : ', curr_word, next_letter, check_word)

        
        # print('-----------------')
        # print('test3 : ', curr_word, next_letter)
        # print('check3 : ', check_word)
        Add_Dict(dictionary, check_word)
        values.append(curr_word+next_letter)
        answer.append(values.index(curr_word)+1)
        i += 1

        if i == len(msg)-1:
            answer.append(values.index(msg[i])+1)

        # print('answer : ', answer)
        # print('dict : ', dictionary)
        # print(i)
    
    return answer


# msg = "TOBEORNOTTOBEORTOBEORNOT"
msg = "KAKAO"
print(solution(msg))