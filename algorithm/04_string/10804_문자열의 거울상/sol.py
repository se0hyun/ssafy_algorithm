char_dict = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}


# def mirror(word):
#     word = word[::-1]
#
#     for i in range(len(word)):
#         word[i] = char_dict.get(word[i])
#
#     return word


def main():
    T = int(input())

    for idx in range(T):
        # res = ''.join(mirror(list(input())))
        print(f'#{idx + 1} {"".join(char_dict.get(c, c) for c in input()[::-1])}')


if __name__ == '__main__':
    main()
