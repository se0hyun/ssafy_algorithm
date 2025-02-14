def main():
    T = int(input())
    for idx in range(T):
        N = int(input())
        matrix = [list(map(int, input().strip())) for _ in range(N)]
        print(f'#{idx + 1} {get_ar(N, matrix)}')


def get_ar(N, matrix):
    # print(matrix)
    sum_ = 0
    for i in range(N // 2 + 1):
        if i == N // 2:
            sum_ += sum(matrix[i][0:N])
            return sum_
        else:
            sum_ += sum(matrix[i][N // 2 - i:N // 2 + i + 1])
            # print(sum_)
            sum_ += sum(matrix[N - 1 - i][N // 2 - i:N // 2 + i + 1])
            # print(sum_)

    return sum_


if __name__ == '__main__':
    main()
