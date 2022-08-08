first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result_list = []
list_length = len(first_list)
i = 0

for i in range(list_length):
    my_tuple = (first_list[i], second_list[i])
    result_list.append(my_tuple)

print(sorted(set(result_list)))