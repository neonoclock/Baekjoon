import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

word = input().strip()

if word == word[::-1]:
    print(1)
else:
    print(0)