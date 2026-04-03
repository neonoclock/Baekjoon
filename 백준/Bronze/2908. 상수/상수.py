import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

A, B = input().split()

A1 = A[::-1]
B1 = B[::-1]

if A1>B1:
    print(A1)
else:
    print(B1)