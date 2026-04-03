import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N = int(input())

numbers = input().strip()

print(sum(map(int, numbers)))