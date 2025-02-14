def is_palindrome(word):    # 주어진 문자열이 회문인지 검사
    if word == word[::-1]:
        return True     # palindrome_count() 메서드에서 if문에 사용됨
    else:               # True, False로 반환
        return False


def palindrome_count(length, matrix):
    MATRIX = len(matrix)
    result = 0
    # 가로(행) 검사
    for i in range(MATRIX):     # 행 고정
        for j in range(MATRIX - length + 1):    # 열 순회하면서
            if is_palindrome(matrix[i][j:j + length]):  # 회문이면
                result += 1                             # 결과 1 증가

    # 세로(열) 검사
    for j in range(MATRIX):     # 열 고정
        for i in range(MATRIX - length + 1):    # 행 순회
            word = ''           # slicing이 어려우므로 빈 문자열에
            for k in range(length):     # 주어진 회문 길이만큼 순회하면서
                word = word + matrix[i + k][j]      # 회문인지 확인할 문자열 생성
            if is_palindrome(word):     # 회문인지 확인
                result += 1

    return result


def main():
    TEST = 10
    MATRIX = 8
    for idx in range(TEST):
        N = int(input())  # 찾아야 하는 회문들의 길이
        table = [list(input()) for _ in range(MATRIX)]

        print(f'#{idx + 1} {palindrome_count(N, table)}')


if __name__ == '__main__':
    main()