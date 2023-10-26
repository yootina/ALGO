# 문자열 배열 strlist가 매개변수로 주어집니다.
# strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

def solution(strlist):
    answer = []

    for i in range(len(strlist)):
        answer.append(len(strlist[i]))

    return answer

print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))


# 프로그래머스 다른 사람의 풀이
def solution(strlist):
    return [len(s) for s in strlist]

print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))
