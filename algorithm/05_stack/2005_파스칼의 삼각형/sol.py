def pascal_triangle(N):
    stack = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1):
            if i == 0 or j == 0 or j == i:
                stack[i].append(1)
            else:
                stack[i].append(stack[i - 1][j - 1] + stack[i - 1][j])

    return stack


def main():
    T = int(input())
    for idx in range(T):
        N = int(input())
        matrix = pascal_triangle(N)

        print(f'#{idx + 1} ')
        for row in matrix:
            print(*row)


if __name__ == '__main__':
    main()
