# 백준 9095번 1,2,3 더하기 : https://www.acmicpc.net/problem/9095

# 접근 1 : 처음에 부분집합으로 해야하나 싶었는데 부분집합 아니라는거 깨달음
# 접근 2 : 규칙성 찾아보기 -> n=1 : 1개, n=2 : 2개, n=3 : 4개, n=4 : 7개, n=5 : 13개 => n=1,2,3일때는 고정이고, 4부터는 n-3,n-2,n-1갯수 더하기?
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return sol(n-3)+sol(n-2)+sol(n-1) # 1,2,3 안들어왔을땐 계속 재귀


tc = int(input())
for i in range(0, tc):
    n = int(input())
    print(sol(n))


