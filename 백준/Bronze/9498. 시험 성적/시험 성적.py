import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

score = int(input())

if 90<=score<=100:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
elif 60<=score<70:
    print("D")
else:
    print("F")