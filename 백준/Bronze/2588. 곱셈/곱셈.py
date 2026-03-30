import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

A = int(input())
B = input().strip()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))