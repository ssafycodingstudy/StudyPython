# 탐욕법lv2 조이스틱 : https://programmers.co.kr/learn/courses/30/lessons/42860

# ord('A') = 65, 영문자는 26개, 14번째부터는 A에서 뒤로 가는게 더 빠름
# jan -> 3개일때 a가 가운데에 1개면 뒤로 가는게 빠름, 1회
# jaan -> 4개일떄 a가 2개면 뒤로 가는게 빠름, 1회
# jabn -> 뒤로 가는게 빠름, 2회
# jban -> 똑같음, 3회
#
# jabbb -> 뒤로가는게 빠름, 3회
# jbabb -> 똑같음, 4회
# jbbab -> 똑같음, 4회
# jaabb -> 뒤로 가는게 빠름, 2회
# jbaab -> 뒤로 가는게 빠름, 3회
# 어짜피 똑같으니, a를 만나면 바로 뒤로 돌아가버리자

def solution(name):
    answer = 0
    next = 0
    last_a = 0

    for i in range(len(name)):
        c = name[i]
        differ = ord(c) - ord('A')
        if differ > 13:  # n을 기준으로 그뒤에 o부터는 a에서 거꾸로 가는게 더 빠름
            differ = abs(differ-26)
        # print(differ)
        answer += differ

        # if i == len(name)-1: # 끝에 도달햇으면
        #     break  # 그냥끝내!
        if c == 'A':
            last_a = i-1
            continue
        elif i+1 < len(name) and name[i+1] == 'A':  # 다음 글자가 A면
            next += last_a
        else:
            next += 1
            if i == len(name)-1:
                break
            # next += 1
    # next -= 1  # 맨 마지막 글자에 도착햇을때 else에서 +1이 한번 되어지기때문에 1만큼 빼주기
    print(next)
    answer += next

    return answer


name1 = "JEROEN"
print(solution(name1))
name2 = "JAN"
print(solution(name2))
name3 = "BBAAABA"
print(solution(name3))  # 7