def inspect_brackets(brackets):
    stack = []
    try:
        for bracket in brackets:
            if bracket in '{(':
                stack.append(bracket)
            elif bracket == '}':
                if stack.pop() == '(':
                    return 0
            elif bracket == ')':
                if stack.pop() == '{':
                    return 0
    except IndexError:
        return 0
    if len(stack) != 0:
        return 0
    return 1


def main():
    T = int(input())
    for idx in range(T):
        print(f'#{idx + 1} {inspect_brackets(input())}')


if __name__ == '__main__':
    main()
