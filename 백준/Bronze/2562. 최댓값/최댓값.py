import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

arr = []

for i in range(9):
    N = int(input())
    arr.append(N)

max_num = max(arr)
idx = arr.index(max_num) + 1

print(max_num)
print(idx)