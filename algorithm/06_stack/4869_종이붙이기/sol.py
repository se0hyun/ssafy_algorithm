def DFS():

    pass


def main():
    T = int(input())
    for idx in range(T):
        print(f'#{idx + 1} {DFS(int(input()))}')


if __name__ == '__main__':
    main()