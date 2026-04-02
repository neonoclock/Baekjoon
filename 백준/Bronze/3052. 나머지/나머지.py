import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

arr = set()

for i in range(10):
    i = int(input())
    0<i<=1000
    n = i%42
    arr.add(n)

print(len(arr))