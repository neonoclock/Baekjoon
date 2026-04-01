import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

X = int(input())
N = int(input())

total = 0

for i in range(1, N+1):
    a, b = map(int, input().split())
    hap = a*b
    total += hap

if total == X:
    print("Yes")
else:
    print("No")