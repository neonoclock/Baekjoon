import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)

    for ch in S:
        print(ch * R, end='')
    print()