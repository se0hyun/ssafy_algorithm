import time
def matrix_max_sum():
    # start = time.time()
    T = 10
    MATRIX = 10
    for tc in range(T):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(MATRIX)]

        start = time.time()
        row_sums = [sum(row) for row in matrix]
        col_sums = [sum(row[i] for row in matrix) for i in range(MATRIX)]
        end = time.time()

        # diagonal sum
        dia_right = 0
        for r, c in zip(range(MATRIX), range(MATRIX)):
            dia_right += matrix[r][c]
        dia_left = 0
        for r, c in zip(range(MATRIX), range(99, -1, -1)):
            dia_left += matrix[r][c]

        print(f'#{tc + 1} {max(max(row_sums), max(col_sums), dia_left, dia_right)}')


def matrix_max_sum_1():
    T = 10
    MATRIX = 10
    for tc in range(T):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(MATRIX)]

        row_sums = [sum(row) for row in matrix]
        print(max(row_sums))
        col_sums = [sum(row[i] for row in matrix) for i in range(MATRIX)]
        print(max(col_sums))

        # diagonal sum
        dia_right = 0
        for r, c in zip(range(MATRIX), range(MATRIX)):
            dia_right += matrix[r][c]
        dia_left = 0
        for r, c in zip(range(MATRIX), range(99, -1, -1)):
            dia_left += matrix[r][c]

        print(f'#{tc + 1} {max(max(row_sums), max(col_sums), dia_left, dia_right)}')


if __name__ == '__main__':
    matrix_max_sum()
    matrix_max_sum_1()
