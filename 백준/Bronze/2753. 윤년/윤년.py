import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

year = int(input())

if year%4==0 and (year%100!=0 or year%400==0):
    print("1")
else:
    print("0")