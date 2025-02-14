def special_sort():
    T = int(input())

    for tc in range(T):
        N = int(input())
        nums = list(map(int, input().split()))

        for i in range(N):
            # print(f'i: {i}')
            min_idx = i
            max_idx = i
            if i % 2 == 0:  # 큰 수 정렬
                for j in range(i+1, N):
                    if nums[j] > nums[max_idx]:
                        max_idx = j
                # print(f'max idx: {max_idx}')
                nums[max_idx], nums[i] = nums[i], nums[max_idx]
            else:   # 작은 수 정렬
                for j in range(i+1, N):
                    if nums[j] < nums[min_idx]:
                        min_idx = j
                # print(f'min idx: {min_idx}')
                nums[min_idx], nums[i] = nums[i], nums[min_idx]
            # print(*nums)
        print(f'#{tc+1}', *nums[0:10])


special_sort()