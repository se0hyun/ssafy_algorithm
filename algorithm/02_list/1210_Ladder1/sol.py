def fine_two(matrix):
    LENGTH = len(matrix)
    for col in range(LENGTH):
        if matrix[LENGTH-1][col] == 2:
            return col


def ladder():
    TESTS = 10
    MATRIX = 100
    dy = [-1, 1]    # 좌 우

    for tc in range(TESTS):
        num = int(input())
        matrix = [list(map(int, input().split())) for _ in range(MATRIX)]
        j = fine_two(matrix)
        for i in range(MATRIX-1, -1, -1):
            for y in dy:
                ny = j + y  # 탐색할 좌 우 열 값
                while (0 <= ny < MATRIX) and matrix[i][ny] == 1:    # 좌 우 값이 조건에 만족하면
                    matrix[i][j] = 0
                    j += y
                    ny += y
            if i == 0:
                end_col = j
        print(f'#{num} {end_col}')


if __name__ == '__main__':
    ladder()

