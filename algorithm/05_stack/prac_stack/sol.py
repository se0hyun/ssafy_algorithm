top = -1
result = [0]*3


def my_push(int_value):
    global top, result
    top += 1
    if top == len(result):
        print('overflow')
    else:
        result[top] = int_value


def my_pop():
    global top, result
    top -= 1
    if top == -1:
        print('underflow')
    else:
        print(result[top + 1])


def main():
    my_push(3)
    my_push(4)
    my_push(5)
    my_pop()
    my_pop()


if __name__ == '__main__':
    main()