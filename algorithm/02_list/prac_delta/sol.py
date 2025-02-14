def delta():
    T = int(input())

    dx = [0, 0, 1, 1]
    dy = [-1, 1, 0, 0]

    for tc in range(T):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(5)]
        new_matrix = [[0 for _ in range(N)] for _ in range(5)]
        total_sum = 0

        for i in range(N):
            for j in range(N):
                abs_sum = 0
                for k in range(4):
                    row_idx = i + dx[k]
                    col_idx = j + dy[k]
                    if 0 <= row_idx < N and 0 <= col_idx < N:
                        diff = matrix[i][j] - matrix[row_idx][col_idx]
                        abs_sum += diff if diff > 0 else -diff

                total_sum += abs_sum

        print(f'#{tc+1} {total_sum}')


if __name__ == '__main__':
    delta()
