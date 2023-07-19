# import numpy as np

def solution(n, computers):
    connected = []
    netCount = 0
    answer = {}

    for i in range(n):
        for j in range(n):
            print(f'i and j are {i}, {j}')

            if i == j and i not in connected:
                netCount += 1
                connected.append(i)
                answer[i] = [i]
                print(f'answer1 is {answer}')
                print(f'connected1 {connected}')
            elif i >= j:
                print('continue')
                continue
            elif computers[i][j] == 1:
                netCount -= 1
                print(f'netCount3 is {netCount}')
                answer[i] = [j]
                connected.append(j)
                print(f'answer3 is {answer}')
                print(f'connected3 {connected}')
            else:
                print('nothing happend')

    return netCount

'''
def solution(n, computers):
    answer = []
    connected = []
    
    for i in range(n):
        for j in range(n):
            print(f'i and j are {i}, {j}')
            print(i in connected)
            if i == j and i not in connected:
                answer.append([i])
                connected.append(i)
                print(f'answer1 {answer}')
                print(f'connected1 {connected}')
                continue
            elif i >= j:
                print('continue')
                continue
            elif computers[i][j] == 1 and j not in connected:
                answer[i].append(j)
                connected.append(j)
                print(f'answer2 {answer}')
                print(f'connected2 {connected}')
            # elif computers[i][j] == 0:
            #     answer.append([j])
            #     connected.append(j)
            #     print(f'answer3 {answer}')
            #     print(f'connected3 {connected}')
        print('---------')
    return len(answer)
'''

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# computers = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# n = 4
# computers = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

print(solution(n, computers))