# 교집합 intersection : set로  해야함 ('list' object has no attribute 'intersection')
def pickMax(list1, list2):
    set1 = set(list1)
    # print(set1)
    set2 = set(list2)
    # print(set1.intersection(set2))
    if len(set1.intersection(set2)) == 0:
        return 0
    return max(set1.intersection(set2))

# print(pickMax([1, 2, 3, 4], [3, 4, 5]))
"""
def findSumList(sampleList):
    sumList = []
    L = len(sampleList)
    print(f'L is {L}')
    for i in range(L):
        print('here', sum(sampleList[:i+1]))
        sumList.append(sum(sampleList[:i+1]))
    return sumList
"""
# print(findSumList(3, [1, 2, 3]))

# 시간 초과!! >>> sumList 다 구한 다음에 최댓값 구하는 거 말고 최대값부터 비교하면서 같은 거 나오면 반환하는 거...!?
def findSumList(sample1, sample2):
    # sample1의 길이가 더 길게
    sum1, sum2 = [], []
    L1, L2 = len(sample1), len(sample2)
    
    i, j = L1, L2

    while i > 0:
        # print(f'i is {i} j is {j}')
        sum1.append(sum(sample1[:i]))
        if j > 0:
            sum2.append(sum(sample2[:j]))
        # print('here', sum1, sum2)
        result = pickMax(sum1, sum2)
        if result > 0:
            # print(result, 'break')
            break
        i -= 1
        j -= 1
        
    # print('here', sum1, sum2)

    return result

def solution(cookie):
    L = len(cookie)
    answer = 0   

    for i in range(L-1):    
        left = cookie[: i+1]
        right = cookie[i+1:]
        # print(f'reverse{list(reversed(left))} right {right}')

        if i <= int(L/2)-1:
            test = findSumList(right, list(reversed(left)))
        else:
            test = findSumList(list(reversed(left)), right)

        if test > answer:
            answer = test

        # maxi = pickMax(leftSum, rightSum)
        # print(f'maxi is {maxi}')
        # if maxi > answer and maxi:
        #     answer = maxi

        print('-----')
    return answer

cookie = [1,1,2,3]
print(solution(cookie))