import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    code = input()
    # print(code)
    stack = []

    for char in code:

        # (, { 를 넣기
        if char == '(' or char == '{':
            stack.append(char)
        
        else:

            if stack[-1] == code[char]:
                stack.pop()
            
            else:
                if char == ')' or char == '}':
                    stack.append(char)
                
    print(stack)

    # 지금까지 작성한걸 print해봐도 내 예상대로 답변이 안나오네..

#####################################################

for tc in range(1, T+1):
    code = input()

    stack = []

    for char in code:
        if char == '(' or char == '{':
            stack.append(char)
        elif len(stack) and char == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) and char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)

    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(result)