T = int(input())  # 반복 횟수

for _ in range(T):
    check = 0
    indx = 0
    s1 = input()
    s2 = s1  # 복사본

    for i in range(int(len(s1)/2)):
        if s1[i] != s1[len(s1)-i-1]:  # 맨앞, 맨뒤에서부터 앞으로오면서 비교
            check = 2  # 대칭이 아니면 해당 인덱스 저장, 체크 표시
            indx = i
            break

    if not check:
        print(0)  # 체크된곳이 없다면 회문이다
    else:
        check = 0
        check1 = 0
        check2 = 0
        indx2 = len(s1)-indx-1  # 체크된 인데스 딱 반대편 위치의 인덱스
        # print(indx, indx2)
        s1 = s1[:indx] + s1[indx+1:]  # 대칭이 아닌 요소는 지우기
        s2 = s2[:indx2] + s2[indx2+1:]
        # print(s1, s2)

        for i in range(int(len(s2)/2)):  # 둘중하나만 회문이면 유사회문
            if s2[i] != s2[len(s2)-i-1]: check1 = 2
            if s1[i] != s1[len(s1)-i-1]: check2 = 2
        if check1 == 2 and check2 == 2:
            check = 2  # 유사회문조차 아님
        if not check:
            print(1)  # 하나가 회문이면 유사회문
        else:
            print(2)
