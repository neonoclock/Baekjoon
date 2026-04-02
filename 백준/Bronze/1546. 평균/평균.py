import sys
input = sys.stdin.readline

# Write your code here
# A, B = map(int, input().split())
# print(A + B)

N = int(input())
score = list(map(int, input().split()))

M = max(score)

new_score = []

for i in range(N):
    new_score.append(score[i]/M*100)

print(sum(new_score)/N)