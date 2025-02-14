def is_palindrome(check, length):
    if check == check[::-1]:
        return True
    else:
        return False


def find_palindrome(matrix, length, target):
    # 행 순회
    for i in range(length):
        for j in range(length - target + 1):
            if is_palindrome(matrix[i][j:j + target + 1], target):
                result = ''.join(matrix[i][j:j + target + 1])
                return result

    # 열 순회
    for j in range(length):
        for i in range(length - target + 1):
            word = ''
            for k in range(target):
                word = word + matrix[i + k][j]
            if is_palindrome(word, target):
                result = word
                return result


def main():
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        table = [list(input()) for _ in range(N)]

        print(f'#{i + 1} {find_palindrome(table, N, M)}')


if __name__ == '__main__':
    main()
