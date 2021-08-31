# 실버3 N과 M(5) : https://www.acmicpc.net/problem/15654
# 순열문제! 수업시간 코드 바탕으로 참고해서 성공

def permutation(length, N, M):
    if length == M:
        print(' '.join(map(str, out)))  # join함수는 ''사이의 구분자를 넣어 리스트의 값과 값 사이를 출력해줌
        return
    for i in range(N):
        if visited[i]: continue

        out.append(a[i])
        visited[i] = True

        permutation(length+1, N, M)
        out.pop()  # pop안해주면 뒤에 계속 붙어서 징그럽게 나옴
        visited[i] = False


N, M = map(int, input().split())
a = list(map(int, input().split()))  # N개 만큼 숫자 입력받아 리스트화
a.sort()  # 오름차순으로 출력해야하니까 미리 정렬

visited = [False] * N
out = []

permutation(0, N, M)
