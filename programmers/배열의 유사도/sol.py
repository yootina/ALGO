# 두 배열이 얼마나 유사한지 확인해보려고 합니다.
# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(s1, s2):
    answer = 0

    for char in s1:
        if char in s2:
            answer += 1
        else:
            continue

    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))


# 프로그래머스 다른사람의 풀이

def solution(s1, s2):
    return len(set(s1)&set(s2))

# set함수에 대해서 다시 공부하게되는 계기.
# set(s1)과 set(s2)를 사용하여 각 문자열을 집합으로 변환하고 set은 중복을 허용하지 않아서 고유한 문자들만 남게되는데
# '&'기호를 사용해 두 집합간의 교집합을 구하고 새로운 집합을 생성한다
# len함수를 사용해서 공통으로 포함된 문자의 개수를 계산해주면 끝이었다.