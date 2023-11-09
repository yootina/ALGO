# 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.


def solution(array):
    answer=[]
    max_array = max(array)
    max_index = array.index(max_array)
    answer = [max_array, max_index]

    return answer



print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))

# sort()로 풀어보려했는데 잘 안풀렸다....


# 다른 사람의 풀이

def solution(array):
    mx = 0
    ind = 0
    for i, v in enumerate(array):
        if v > mx:
            mx = v
            ind = i
    return [mx, ind]

# enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)을 만들어준다.
# enumerate() 함수 쓸 생각을 기본적으로 하지 못했다.


