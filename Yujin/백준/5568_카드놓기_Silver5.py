import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
K = int(input())
cards = []

for _ in range(N):
    cards.append(input().rstrip())

result = set()
for card in permutations(cards, K):
    result.add(''.join(card))

print(len(result))
