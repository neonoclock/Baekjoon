import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break