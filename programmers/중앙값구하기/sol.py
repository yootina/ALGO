# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다.
# 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다.
# 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    answer = 0
    array.sort()
    center_idx = len(array)//2
    answer = array[center_idx]

    return answer


print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))

# 프로그래머스 다른 사람의 풀이

def solution(array):
    return sorted(array)[len(array) // 2]
# 이렇게 짧게 쓰는것도 가능하다니...