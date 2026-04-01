import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

while True:
    A, B = map(int, input().split())
    if A==0 and B==0:
        break
    else:
        print(A+B)