# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
# 정수 배열 array가 매개변수로 주어질 때,
# 최빈값을 return 하도록 solution 함수를 완성해보세요.
# 최빈값이 여러 개면 -1을 return 합니다.

def solution(array):
    count = [0] * (max(array)+1)

    for i in array:
        count[i] += 1
    
    number = 0
    for j in count:
        if j == max(count):
            number += 1
    
    if number > 1:
        return -1
    else:
        return count.index(max(count))

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))

# 프로그래머스 다른 사람의 풀이

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))

# 배열 array의 길이가 0이 아닌동안 반복을 하고,
# array를 set를 통해 묶어줌으로써 중복을 제거한 집합을 만들고
# 각 요소를 enumerate하여 i, a에 각각 넣어준다.
# a를 remove()함수를 써주면서 해당 인덱스가 아니라 값을 써주고 그 값을 지워줬다.
# 파이썬 튜터를 돌려보니 값을 지우고 리스트내에서 데이터가 재정렬이 되었다.
# 해당 인덱스값이 0일 때 a값을 반환하고 최빈값인 a를 반환한다.

# pop()함수는 해당 인덱스값을 지우기때문에 remove()함수가 적절하다.

# - remove() 함수: 리스트에서 지정된 값을 찾아 첫 번째로 일치하는 값을 제거. 즉, 값에 따라 제거하고자 하는 요소를 찾아서 제거.
# - pop()함수: 리스트에서 지정된 인덱스에 있는 요소를 제거하고 해당 요소를 반환. 이 함수는 인덱스를 사용하여 요소를 제거.