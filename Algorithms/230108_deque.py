"""
1 xxx : Deque의 앞쪽에 x를 추가한다.
2 xxx : Deque의 뒤쪽에 x를 추가한다.
3 : Deque에 가장 앞쪽의 원소를 삭제한다. 만약 Deque에 원소가 없다면 연산은 무시된다.
4 : Deque에 가장 뒤쪽의 원소를 삭제한다. 만약 Deque에 원소가 없다면 연산은 무시된다.
5 : Stack에 가장 앞쪽의 원소를 출력한다. 만약 Stack에 원소가 없다면 −1-1−1을 출력한다.
6 : Stack에 가장 뒤쪽의 원소를 출력한다. 만약 Stack에 원소가 없다면 −1-1−1을 출력한다.
7 : Stack에 존재하는 원소의 개수를 출력한다.
"""

N = 3
stack = []

def calculation(value):
    print('check')
    if value[0] == '1':
        print('check1')
        stack.insert(0, int(value[1]))    #특정 위치 원소 추가
        return stack

    elif value[0] == '2':
        print('check2')
        stack.append(int(value[1]))    # 가장 뒤에 원소 추가
        return stack

    elif value[0] == '3':
        if len(stack)>0:
            del stack[0]    # del : 특정 위치 원소 삭제
        return stack
    
    elif value[0] == '4':
        if len(stack)>0:
            stack.pop()    # pop 가장 뒤쪽 원소 삭제
        return stack

    elif value[0] == '5':
        if len(stack) == 0:
            return -1
        return stack[0]

    elif value[0] == '6':
        if len(stack) == 0:
            return -1
        return stack[-1]    # 가장 뒤쪽의 원소

    elif value[0] == '7':
        return len(stack)

    
# ---- 파이썬은 함수 선언 순서도 중요하다 ---- #    

for i in range(N):
    order = input().split(' ')
    # print(order)

    stack = calculation(order)
    if int(order[0])>=5:
            print(stack)

# print(stack)