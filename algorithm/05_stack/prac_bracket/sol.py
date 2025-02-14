def is_bracket(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return -1
            else:
                stack.pop()
    if len(stack) > 0:
        return -1
    return 1


def main():
    T = int(input())

    for idx in range(T):
        print(f'#{idx+1} {is_bracket(list(input()))}')


if __name__ == '__main__':
    main()