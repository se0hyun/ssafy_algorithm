# 버블 정렬

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
print(bubble_sort([4, 2, 48, 24, 5, 234, 63, 948, 12, 74]))