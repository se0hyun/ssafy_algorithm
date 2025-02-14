def fast_typing(origin, shortcut):
    originLength = len(origin)  # 원본 문자열 길이
    shortcutLength = len(shortcut)  # 단축어 길이
    result = 0
    i = 0

    while i < originLength:
        try:
            if origin[i:i+shortcutLength] == shortcut:
                result += 1
                i += shortcutLength
            else:
                result += 1
                i += 1
        except IndexError:
            result += originLength - i
    return result


def main():
    T = int(input())
    for idx in range(T):
        str1, str2 = map(str, input().split())

        print(f'#{idx + 1} {fast_typing(str1, str2)}')


if __name__ == '__main__':
    main()
