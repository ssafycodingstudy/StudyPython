# 이미 펠린드롬을 만족하는 부분빼고, 그 나머지 부분을 뒤에다가 붙여주면됨.

s = input()  # 문자열 입력

for i in range(len(s)):
    #  깔끔하게 처리하는 방법 찾아보다가 발견한건데 2번째 슬라이싱 방법 구조는 처음봄
    print(s[i::-1])  # 앞에서부터 i개만큼 거꾸로 출력
    print(s[i:][::-1])  # len(s)-i개만큼 거꾸로 출력
    print(s[::-1]) # 그냥 거꾸로 출력
    if s[i:] == s[i:][::-1]:
        print(len(s)+i)
        break
    print("--------------")
