# 백준 실버1 Moo게임
N = int(input())
arr = [0 for _ in range(28)]
arr[0] = 3
arr[1] = 10
arr[2] = 25

for i in range(3, 28):
    arr[i] = arr[i-1]*2 + (i+3)

def divide(n):
    if n <= 3: # moo의 범위안으로 들어올때
        if n == 1:
            return "m"
        else:
            return "o"
    for i in range(28):
        if n <= arr[i]:
            index = i
            break
    n -= arr[index-1] # 이전 moo배열보다 오른쪽에 위치할 수 밖에 없음
    if n <= index + 3: # 가운데 위치할때
        if n == 1:
            return "m"
        else:
            return "o"
    n -= (index + 3) # 가운데보다 오른쪽에 위치하면 이전 배열의 길이보다 작게 함
    return divide(n)

print(divide(N))
 
