import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

n = int(input())

total = 0

for i in range(1, n+1):
    total += i

print(total)