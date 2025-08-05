def merge_digit_intervals(input_list: list) -> list:
    if not input_list:
        return []
    
    input_list.sort()
    output_list = [input_list[0]]

    for i in input_list[1:]:
        last_one = output_list[-1]

        if i[0] <= last_one[1]:
            last_one[1] = max(last_one[1], i[1])
        else:
            output_list.append(i)

    return output_list

input_list = [[1, 3], [2, 6], [9, 11], [8, 9], [2, 5], [10, 15], [16, 19]]
output_list = merge_digit_intervals(input_list)
print("input_list:", input_list)
print("output_list:", output_list)