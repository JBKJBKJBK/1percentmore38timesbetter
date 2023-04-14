def Hanoi(N):
    if N == 1:
        return 1
    return 2 * Hanoi(N-1) + 1

N = 2
N = 3
print(Hanoi(N))
