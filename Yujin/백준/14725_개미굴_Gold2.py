import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        cur[0] = True

    def under(self, lev, cur):
        if 0 in cur:
            return

        cur_child = sorted(cur)

        for child in cur_child:
            print("--"*lev + child)
            self.under(lev+1, cur[child])

N = int(input().strip())
nest = Trie()
for _ in range(N):
    line = input().split()
    K = line[0]
    foods = line[1:]
    nest.add(foods)
nest.under(0, nest.root)