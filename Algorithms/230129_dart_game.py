#'점수, 보너스문자, 옵션문자'로 나누어 리스트로 변경
def preprocessing(input, score_range, bonus_letter, option_letter):
    # score_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    dart_string = input
    dart_list = []
    # print(dart)
    while len(dart_string)>0:
        if dart_string[:2] in score_range:
            # print(dart_string[:2])
            dart_list.append(int(dart_string[:2]))
            dart_string = dart_string[2:]
        elif dart_string[0] in score_range:
            dart_list.append(int(dart_string[0]))
            dart_string = dart_string[1:]
        else:
            dart_list.append(dart_string[0])
            dart_string = dart_string[1:]
        # print(dart_string, dart_list)
    return dart_list

#보너스 함수
def Bonus(num, bonus_letter):
    if bonus_letter == 'S':
        return num
    elif bonus_letter == "D":
        return num**2
    elif bonus_letter == "T":
        return num**3

#옵션 함수
def Option(option_letter, score_list):
    if option_letter == '*':
        if len(score_list) >= 2:
            score_list[-1] *= 2
            score_list[-2] *= 2
        else:
            score_list[-1] *= 2
        return score_list
    elif option_letter == '#':
        score_list[-1] *= -1
    print(score_list)
    return score_list

def solution(dartResult):
    score_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    bonus_letter = ['S', 'D', 'T']
    option_letter = ['*', '#']

    #'점수, 보너스문자, 옵션문자'로 나누어 리스트로 변경
    dart_list = preprocessing(dartResult, score_range, bonus_letter, option_letter)
    # print(dart_list)
    
    result = []
    for idx in range(len(dart_list)):
        if dart_list[idx] in bonus_letter:
            score = Bonus(int(dart_list[idx-1]), dart_list[idx])
            result.append(score)
            print('Bonus :' , result)
        if dart_list[idx] in option_letter:   
            result = Option(dart_list[idx], result)
            print('Option: ', result)
    answer = sum(result)
    return answer

# dartResult = "1S2D*3T"
# dartResult = "1D2S#10S"
dartResult = "1S*2T*3S"
print('The answer is: ' , solution(dartResult))
