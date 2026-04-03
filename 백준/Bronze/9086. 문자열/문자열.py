import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

T = int(input())

for i in range(T):
    A = input().strip()
    print(A[0]+A[-1])