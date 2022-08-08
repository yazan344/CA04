first_list = [3, 6, 9, 12, 15, 18, 21]
second_list = [4, 8, 12, 16, 20, 24, 28]
result_list = []

for i in range(len(first_list)):
    if i % 2 == 0 :
        result_list.append(first_list[i])
    else:
        result_list.append(second_list[i])

print(result_list)