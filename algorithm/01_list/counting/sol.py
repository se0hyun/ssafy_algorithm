def counting_sort(origin_list):
    max_value = max(origin_list)
    length = len(origin_list)
    result = [0 for _ in range(length)]
    count_list = [0 for _ in range(max_value + 1)]

    for i in origin_list:
        count_list[i] += 1
    print(f'count list: {count_list}')

    for i in range(1, max_value + 1):
        count_list[i] += count_list[i - 1]
    print(f'sum list: {count_list}')

    # for element in origin_list:
    #     result[count_list[element]-1] = element
    #     count_list[element] -= 1

    # for i in range(length - 1, -1, -1):
    for i in reversed(origin_list):
        count_list[origin_list[i]] -= 1
        result[count_list[origin_list[i]]] = origin_list[i]

    return result


if __name__ == '__main__':
    print(counting_sort([1, 3, 4, 2, 1, 1, 3]))
    print(counting_sort([1, 3, 4, 2, 1, 1, 3, 0, 0]))
