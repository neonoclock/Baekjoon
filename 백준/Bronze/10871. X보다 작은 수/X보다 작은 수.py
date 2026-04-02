import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N, X = map(int, input().split())
A = list(map(int, input().split()))

arr = []

for i in range(N):
    if A[i] < X:
        arr.append(A[i])
print(*arr)
