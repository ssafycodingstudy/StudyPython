character = "10 5 2"
monsters = ["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"]
# 반례찾기

# "10 5 2"	["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"]	"Beginner"
def solution(character, monsters):
    character = list(map(int, list(character.split(" "))))
    for i in range(len(monsters)):
        monsters[i] = list(monsters[i].split(" "))
        monsters[i][1:] = list(map(int, list(monsters[i][1:])))

    exp = dict()
    for i in range(len(monsters)):
        time = 0
        flag = True
        while monsters[i][2] > 0:
            time += 1
            attack = monsters[i][4] - character[1]
            if attack >= 0:
                flag = False
                break
            else:
                monsters[i][2] += attack
                if monsters[i][2] <= 0:
                    break
            c_attack = character[2] - monsters[i][3]
            if c_attack < 0:
                if character[0] + c_attack <= 0:
                    flag = False
                    break
        if flag:
            exp[monsters[i][0]] = [monsters[i][1], time]

    result = []
    maxM = 0
    for mon in exp.keys():
        maxM = max(maxM, exp[mon][0]/exp[mon][1])
        result.append([mon, exp[mon][0]/exp[mon][1]])

    for i in range(len(result)):
        if maxM == result[i][1]:
            return result[i][0]

print(solution(character, monsters))