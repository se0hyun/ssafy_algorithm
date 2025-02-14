def coloring():
    T = int(input())

    for tc in range(T):
        N = int(input())
        matrix = [[0 for _ in range(10)] for _ in range(10)]
        purple_cnt = 0

        '''
        2
        2 2 4 4 1
        3 3 6 6 2
        '''
        for i in range(N):
            r1, c1, r2, c2, color_code = map(int, input().split())  # start row/col, end row/col

            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if matrix[r][c] != color_code:
                        matrix[r][c] += color_code
                    if matrix[r][c] not in [0, 1, 2]:
                        purple_cnt += 1
        print(f'#{tc+1} {purple_cnt}')


if __name__ == '__main__':
    coloring()
