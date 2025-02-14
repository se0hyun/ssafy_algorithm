def is_palindrome(tc, word):
    LENGTH = len(word)
    word = list(word)

    for i in range(LENGTH // 2):
        if word[i] == word[LENGTH - 1 - i]:
            continue
        else:
            return f'#{tc+1} 0'
    return f'#{tc+1} 1'


def main():
    T = int(input())
    for i in range(T):
        case = input()
        print(is_palindrome(i, case))


if __name__ == '__main__':
    main()