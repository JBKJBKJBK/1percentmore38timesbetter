from string import punctuation
"""
자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 
두 집합 A, B 사이의 자카드 유사도 J(A, B)는 
두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.

예를 들어 집합 A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때, 
교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로, 
집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다. 
집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
"""

str1 = "aa1+aa2"
str2 = "AAAA12"

# str1 = "handshake"
# str2 = "shake hands"

# str1 = 'France'
# str2 = 'french'



# ---- 61.5점. hidden case 가 있는 듯 하다. ----
def newsClustering(str1, str2):
    # 소문자로 변환
    str1 = str1.lower()
    str2 = str2.lower()
    print(str1, str2)

    #특수문자 제거 >> 여기서 제거가 아님
    # for symbol in punctuation:
    #     str1 = str1.replace(symbol, '')
    #     str2 = str2.replace(symbol, '')
    # print(str1, str2)

    str1_list = [str1[i]+str1[i+1] for i in range(len(str1)-1) if str1[i].islower() and str1[i+1].islower()]
    str2_list = [str2[i]+str2[i+1] for i in range(len(str2)-1) if str2[i].islower() and str2[i+1].islower()]
    # filtered_str1_list, filtered_str2_list = set(str1_list), set(str2_list)
    print(str1_list, str2_list)
    print(len(str1_list), len(str2_list))

    if len(str1_list) + len(str2_list) == 0:
        return 65536

    count_common = 0
    for element in str1_list:
        if element in str2_list:
            str2_list.remove(element)    #여기 부분으로 hidden case 해결. 
            count_common += 1
        print(str2_list)

    count_total = len(str1_list) + len(str2_list)
    print(count_common, count_total)

    # if count_total == 0:
    #     return 65536 * 1

    similarity =  count_common / count_total

    return int(65536 * similarity)

print(newsClustering(str1, str2))

# 파이썬 합집합,교집합