#2019 카카오 개발자 겨울 인턴십

# 함수로 정리해보기

# ---- 프로그래머스 제출 코드 ----

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

s = s.replace('{', '').replace('}', '')
# print(s)
to_list = s.split(',')
# print(to_list)

result = {}
for ele in to_list:
    result[ele] = to_list.count(ele)
# print(result)

sorted_result = sorted(result, key=lambda x:result[x], reverse=True)
answer = tuple(int(num) for num in sorted_result)
# print(answer)

# ---- 연습장 ----
# from collections import Counter

# '{', '}' 지우기
# to_list = s.split('},{')
# print(to_list)

# new_list = []
# for element in to_list:
#     print(element)
#     new_e = element.replace('{', '').replace('}', '')
#     print(new_e)
#     new_list.append(new_e)
#     # new_e = list(new_e)
#     # print(new_e)

# print(new_list)

# target = new_list[0]
# for ele in new_list:
#     if len(ele) > len(target):
#         target = ele
# target = target.split(',')
# print(target)

# target_list = [int(num) for num in target]
# print(tuple(target_list))