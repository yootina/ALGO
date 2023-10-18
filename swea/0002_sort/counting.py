my_list = [1, 10, 4, 7, 8, 3, 1, 9, 2, 4]

# 1.couter 리스트 만들어주기(리스트 컴플레이션)

counter = [0 for i in range(10)]

for num in my_list:
    counter[num] += 1

    # print(counter)

result = []

for value, count in enumerate(counter):
    # print(value, count)
    for i in range(count):
        result.append(value)

print(result)
