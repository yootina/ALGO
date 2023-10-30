# 문자열 str1, str2가 매개변수로 주어집니다.
# str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(str1, str2):
    answer = 0

    for char in str1:
        if str2 in str1:
            answer = 1
        else:
            answer = 2
    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))

# 프로그래머스 다른사람의 풀이

def solution(str1, str2):
    return 1 + int(str2 not in str1)

# 저번 int의 응용.

