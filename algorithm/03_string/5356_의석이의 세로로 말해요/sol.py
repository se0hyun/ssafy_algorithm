def read_vertical(matrix):
    max_length = 0
    result = ''
    for i in range(5):
        max_length = max(max_length, len(matrix[i]))
    for j in range(max_length):
        for i in range(5):
            try:
                result = result + matrix[i][j]
            except IndexError:
                continue
    return result


def main():
    T = int(input())
    for i in range(T):
        table = [[c for c in input()] for _ in range(5)]

        print(f'#{i + 1} {read_vertical(table)}')


if __name__ == '__main__':
    main()
