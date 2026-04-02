import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N = int(input())
arr = list(map(int, input().split()))
v = int(input())

cnt = 0

for i in range(N):
    if arr[i] == v:
        cnt += 1
print(cnt)        