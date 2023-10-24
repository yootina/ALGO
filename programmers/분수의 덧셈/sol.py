# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
# 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
# 두 분수를 더한 값을 기약 분수로 나타냈을 때
# 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

import math

def solution(numer1, denom1, numer2, denom2):
    
    boonmo = denom1 * denom2
    boonza = (numer1 * denom2) + (denom1 * numer2)
    gcd_number = math.gcd(boonmo, boonza)

    answer = [boonza // gcd_number, boonmo // gcd_number]

    return answer


print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))

# math.gcd() 함수를 이용하면 최대공약수를 쉽게 구할 수 있었다.

###########################################################

# 다른 사람의 풀이

from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))


# fractions는 유리수를 계산할 때 사용하는 모듈
# from fractions import Fraction
# 분자의 값은 numerator (a.numerator)
# 분모의 값은 denominator (a.denominator)

#################################################

# 모듈을 쓰지 않은 다른 풀이

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(denum1, num1, denum2, num2):
    # 1. 두 분수의 합 계산
    boonmo = num1 * num2
    boonja = denum1 * num2 + denum2 * num1
    
    # 2. 최대공약수 계산
    gcd_value = gcd(boonmo, boonja)

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer