import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

count = 0

while count < 100:
    try:
        A = input().strip()
    except:
        break
    print(A)
    count += 1