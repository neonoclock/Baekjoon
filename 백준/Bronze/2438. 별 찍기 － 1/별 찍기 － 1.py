import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N = int(input())

for i in range(1, N+1):
    for j in range(i):
        print("*", end="")
    print()