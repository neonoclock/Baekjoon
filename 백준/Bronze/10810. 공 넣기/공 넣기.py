import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N, M = map(int, input().split())

basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        basket[x] = k
print(*basket)

