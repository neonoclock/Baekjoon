import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N = int(input())

for i in range(1, N+1):
    print(" "*(N-i)+("*"*i))