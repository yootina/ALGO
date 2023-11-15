# 문자열 myString이 주어집니다.
# myString을 문자 "x"를 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

def solution(myString):
    answer = []
    str_list = myString.split('x')

    for string in str_list:
        answer.append(len(string)) # ['o', 'oo', 'o', '', 'o', '']
    return answer


print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))



# 다른 사람의 풀이
# 람다함수를 잘 몰라서 한번 적어 보았다.
def solution(myString):
    return list(map(lambda x: len(x), myString.split('x')))