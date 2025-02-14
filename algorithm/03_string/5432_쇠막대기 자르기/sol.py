def steel_stick(marks):
    stack = []
    stick = 0

    for i in range(len(marks)):
        if marks[i] == '(':
            stack.append(marks[i])
        else:
            if marks[i - 1] == '(':
                stack.pop()
                stick += len(stack)
            else:
                stack.pop()
                stick += 1
    return stick


def main():
    T = int(input())
    for i in range(T):
        case = [c for c in input()]

        print(f'#{i + 1} {steel_stick(case)}')


if __name__ == '__main__':
    main()
