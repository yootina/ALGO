# 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

# - 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(sides):
    
    sides.sort()

    if sides[2] >= sides[1] + sides[0]:
        return 2
    else:
        return 1


print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))


# 다른 사람의 풀이

def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

# 이렇게까지 생각은 했는데 어떻게 구현할지 몰랐다.
# sides의 최댓값이 sides의 더한값에서 최댓값을 뺐을 때 작으면 되는데 왜 코드로 생각이 안났을까.