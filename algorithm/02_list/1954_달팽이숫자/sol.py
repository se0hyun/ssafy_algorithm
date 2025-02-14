def snailNumber():
    T = int(input())

    for tc in range(T):
        N = int(input())
        matrix = [[0 for _ in range(N)] for _ in range(N)]
        # dx = [0, 1, 0, -1]  # 우 하 좌 상
        # dy = [1, 0, -1, 0]  # 우 하 좌 상
        i, j = 0, 0
        num = 0

        while num < N*N:
            if (j - 1 < 0 or matrix[i][j - 1] != 0) and (i - 1 < 0 or matrix[i - 1][j] != 0):  # 우
                while j < N and matrix[i][j] == 0:
                    num += 1
                    matrix[i][j] = num
                    j += 1
                j -= 1
                i += 1
            elif (j + 1 >= N or matrix[i][j + 1] != 0) and (i - 1 < 0 or matrix[i - 1][j] != 0):  # 하
                while i < N and matrix[i][j] == 0:
                    num += 1
                    matrix[i][j] = num
                    i += 1
                i -= 1
                j -= 1
            elif (j + 1 >= N or matrix[i][j + 1] != 0) and (i + 1 >= N or matrix[i + 1][j] != 0):  # 좌
                while j >= 0 and matrix[i][j] == 0:
                    num += 1
                    matrix[i][j] = num
                    j -= 1
                j += 1
                i -= 1
            elif (j - 1 < 0 or matrix[i][j - 1] != 0) and (i + 1 >= N or matrix[i + 1][j] != 0):  # 상
                while i >= 0 and matrix[i][j] == 0:
                    num += 1
                    matrix[i][j] = num
                    i -= 1
                i += 1
                j += 1

        print(f'#{tc+1}')
        for row in matrix:
            print(*row)

snailNumber()