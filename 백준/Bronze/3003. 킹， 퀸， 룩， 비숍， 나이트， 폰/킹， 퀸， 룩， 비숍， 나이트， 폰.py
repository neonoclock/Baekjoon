import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

K, Q, L, B, N, P = map(int, input().split())

print(1-K, 1-Q, 2-L, 2-B, 2-N, 8-P)