import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A+B}")