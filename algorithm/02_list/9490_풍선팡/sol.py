def balloon(matrix, N, M):
    dx = [0, 0, -1, 1]  # 우 좌 하 상
    dy = [1, -1, 0, 0]
    max_sum = 0
    for i in range(N):
        for j in range(M):
            result = matrix[i][j]
            value = matrix[i][j]
            for dir_x, dir_y in zip(dx, dy):
                for k in range(1, value + 1):
                    nx = i + dir_x * k
                    ny = j + dir_y * k
                    if 0 <= nx < N and 0 <= ny < M:
                        result += matrix[nx][ny]
            max_sum = max(max_sum, result)
    return max_sum


def main():
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        table = [list(map(int, input().split())) for _ in range(N)]
        print(f'#{i + 1} {balloon(table, N, M)}')


if __name__ == '__main__':
    main()
