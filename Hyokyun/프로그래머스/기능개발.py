def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    counts = [0] * len(progresses)
    for i in range(n):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            counts[i] += 1
    count = 0
    for i in range(n):
        if counts[i] == 0:
            continue
        count += 1
        for j in range(i + 1, n):
            if counts[i] < counts[j]:
                break
            if counts[i] >= counts[j]:
                count += 1
                counts[j] = 0
        counts[i] = 0
        answer.append(count)
        count = 0
    return answer