import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

arr = []

for _ in range(28):
    n = int(input())
    arr.append(n)

student = []

for i in range(1, 31):
    if i not in arr:
        print(i)
