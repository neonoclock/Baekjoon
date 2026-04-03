import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

S = input().strip()

for i in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(i), end=' ')