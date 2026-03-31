import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)


A, B = map(int, input().split())
C = int(input())

D = B-C


total = (A * 60 + B + C) % 1440
print(total // 60, total % 60)