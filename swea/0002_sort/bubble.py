my_list = [1, 10, 4, 7, 8, 3, 1, 9, 2, 4]


for i in range(len(my_list)-1, 0, -1): #인덱스 검증
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        # print(left, right)
        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1],  my_list[j]
    