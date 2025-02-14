def del_repeated_char(string):
    stack = []
    for i in range(len(string)):
        try:
            if string[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(string[i])
        except IndexError:
            stack.append(string[i])
    return len(stack)


def main():
    T = int(input())
    for idx in range(T):
        print(f'#{idx + 1} {del_repeated_char(list(input()))}')


if __name__ == '__main__':
    main()
