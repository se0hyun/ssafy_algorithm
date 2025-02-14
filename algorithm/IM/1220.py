import sys
sys.stdin = open('input (3).txt')

def count_magnetic(matrix):
    """ 위에서 아래로 떨어지는 자성체를 시뮬레이션하여 교착 상태 개수를 세는 함수 """
    N = len(matrix)
    count = 0

    for col in range(N):  # 열(column) 기준으로 탐색
        prev_magnet = 0  # 이전에 만난 자석 상태 (0: 없음, 1: S극, 2: N극)

        for row in range(N):  # 위에서 아래로 스캔
            if matrix[row][col] == 1:  # S극 (아래로 이동)
                prev_magnet = 1  # S극 발견
            elif matrix[row][col] == 2:  # N극 (위로 이동)
                if prev_magnet == 1:  # 바로 위에 S극이 있으면 교착 상태 발생
                    count += 1
                prev_magnet = 2  # N극 발견

    return count

def main():
    T = 10
    MATRIX = 100
    for idx in range(T):
        length = int(input())
        arr = [list(map(int, input().split())) for _ in range(MATRIX)]
        print(f'#{idx + 1} {count_magnetic(arr)}')

        '''1은 S극으로
        2는 N극으로 끌림'''


if __name__ == '__main__':
    main()

# def rotate(matrix):
#     length = len(matrix)
#     arr = [[0] * length for _ in range(length)]  # 빈 배열 생성
#
#     for i in range(length):
#         for j in range(length):
#             arr[j][length - i - 1] = matrix[i][j]  # 회전 공식 수정
#
#     return arr  # 결과 반환
#
#
# def magnetic(length, matrix):
#     matrix = rotate(matrix)
#     new_matrix = [row[:] for row in matrix]
#
#     s_removed = [[0] * length for _ in range(length)]
#     n_removed = [[0] * length for _ in range(length)]
#
#     for i in range(length):
#         for j in range(length):
#             if matrix[i][j] == 1:
#                 if j > 0 and 2 not in matrix[i][:j]:
#                     new_matrix[i][j] = 0
#                     # s_removed[i][j] = 0
#                 elif j == 0:
#                     new_matrix[i][j] = 0
#
#             elif matrix[i][j] == 2:
#                 if j < length-1 and 1 not in matrix[i][j+1:]:
#                     new_matrix[i][j] = 0
#                 elif j == length - 1:
#                     new_matrix[i][j] = 0
#
#     # count = 0
#     return sum(row.count(1) for row in new_matrix) + sum(row.count(2) for row in new_matrix)
#
#     # return count