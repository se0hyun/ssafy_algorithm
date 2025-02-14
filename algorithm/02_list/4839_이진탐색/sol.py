def binarySearch():
    T = int(input())
    for tc in range(T):
        P, Pa, Pb = map(int, input().split())

        def search(target):
            start, end, cnt = 1, P, 0
            while start <= end:
                middle = (start + end) // 2
                cnt += 1
                if middle < target:
                    start = middle + 1
                elif middle > target:
                    end = middle - 1
                else:
                    return cnt

        count_A = search(Pa)
        count_B = search(Pb)

        if count_A > count_B:
            print(f'#{tc + 1} B')
        elif count_A < count_B:
            print(f'#{tc + 1} A')
        else:
            print(f'#{tc + 1} 0')


if __name__ == '__main__':
    binarySearch()
