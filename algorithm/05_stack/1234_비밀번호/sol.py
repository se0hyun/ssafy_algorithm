def get_password(N, password):
    stack = []
    for i in range(int(N)):
        try:
            if password[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(password[i])
        except IndexError:
            stack.append(password[i])

    return ''.join(stack)


def main():
    T = 10
    for idx in range(T):
        length, password = input().split()
        print(f'#{idx + 1} {get_password(length, password)}')


if __name__ == '__main__':
    main()