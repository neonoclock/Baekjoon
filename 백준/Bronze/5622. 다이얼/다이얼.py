import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

word = input().strip()

total = 0

for ch in word:
    if ch in 'ABC':
        total += 3
    elif ch in 'DEF':
        total += 4
    elif ch in 'GHI':
        total += 5
    elif ch in 'JKL':
        total += 6
    elif ch in 'MNO':
        total += 7
    elif ch in 'PQRS':
        total += 8
    elif ch in 'TUV':
        total += 9
    elif ch in 'WXYZ':
        total += 10
    else:
        total += 11

print(total)
    