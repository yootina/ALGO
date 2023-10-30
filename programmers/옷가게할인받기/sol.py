# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

def solution(price):
    
    if 100000 <= price < 300000:
        return int(price - (price * 0.05))
    elif 300000 <= price < 500000:
        return int(price -(price * 0.1))
    elif 500000 <= price:
        return int(price -(price * 0.2))
    else:
        return price


print(solution(150000))
print(solution(580000))

# Q. 왜 난 노가다밖에 생각이 안날까...
# Q. 처음에 풀때는 return 값에 할당한게 아니라 answer에 값을 할당했는데 정답이 아니라고 나왔다.
# A. 아, return 값에 값을 할당하지 않아서가 아니라 10만원 미만을 안챙겨서 그렇구나.

def solution(price):
    answer = 0

    if 100000 <= price < 300000:
        answer = int(price - (price * 0.05))
    elif 300000 <= price < 500000:
        answer = int(price -(price * 0.1))
    elif 500000 <= price:
        answer = int(price -(price * 0.2))
    
    return answer