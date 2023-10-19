import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = list(map(str, input()))

    stack = []
    # print(string)

    for i in range(len(string)):

        # stack에 아무런 값도 들어가 있지 않을때
        if not stack:
            stack.append(string[i])

        # stack에 값이 들어가있을 때
        else:

            # stack의 마지막글자가 추가하려는 글자와 같다면 없애준다
            if stack[-1] == string[i]:
                stack.pop()
            
            # 아니라면 stack의 리스트에 더해준다
            else:
                stack.append(string[i])
    
    result = len(stack)
    
    print(f'#{tc} {result}')

#############################################################################

for tc in range(1, T+1):
    string = input()

    stack = []

    for char in string:
        # 스택이 비어있는 경우
        if len(stack) == 0:
            stack.append(char)
        # 스택이 비어있지 않은경우 => 비교를 할 수 있는 상태
        else:
            # 제일 마지막 데이터와 비교하는 데이터가 일치하는경우
            if char == stack[-1]:
                stack.pop()
            # 일치하지 않은경우
            else:
                stack.append(char)

    print(stack)   