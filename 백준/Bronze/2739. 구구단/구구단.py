import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N = int(input())

for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")