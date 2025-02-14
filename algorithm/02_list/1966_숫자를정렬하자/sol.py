def selection_sort():
    T = int(input())

    for tc in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        length = len(nums)

        for i in range(length):
            idx = i
            for j in range(i + 1, length):
                if nums[j] < nums[idx]:
                    idx = j
                nums[i], nums[idx] = nums[idx], nums[i]

        print(*nums)


selection_sort()

def bubble_sort():
    T = int(input())

    for tc in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        length = len(nums)

        for i in range(length):
            pass
