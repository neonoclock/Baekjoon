import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N = int(input())

arr = []

row = list(map(int, input().split()))

arr.extend(row)

print(min(arr), max(arr))