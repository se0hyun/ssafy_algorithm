class get_all_subset:

    # 비트 연산
    def bit_calculate(self):
        T = int(input())

        for tc in range(T):
            N = int(input())
            nums = list(map(int, input().split()))

            cnt = 0
            for i in range(1 << N):
                subset_sum = 0
                for j in range(N):
                    if i & (1 << j):
                        subset_sum += nums[j]
                    

    # 2. 재귀
    def recursive(self):
        pass
