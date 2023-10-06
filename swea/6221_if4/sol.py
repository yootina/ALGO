import sys
sys.stdin = open('input.txt', encoding='utf-8')

Man1 = input()
Man2 = input()

rcp = ['가위', '바위', '보']

Man1_idx = rcp.index(Man1)
Man2_idx = rcp.index(Man2)

# print(Man1_idx, Man2_idx)

result = Man1_idx - Man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    print(f'Result : Man{result+3} Win!')