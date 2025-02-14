def is_palindrome(word):    # 주어진 문자열이 회문인지 검사
    if word == word[::-1]:
        return True     # palindrome_count() 메서드에서 if문에 사용됨
    else:               # True, False로 반환
        return False


def find_longest_palindrome(matrix):
    MATRIX = len(matrix)
    max_len = 0
    # 가로(행) 검사
    for i in range(1, MATRIX):  # 행 고정
        for length in range(MATRIX):     # 직선 회문의 최대 길이는 행렬의 길이
            for j in range(MATRIX - length + 1):  # 열 순회하면서
                if is_palindrome(matrix[i][j:j + length]):  # 회문이면
                    max_len = max(max_len, length)  # 결과 1 증가

    # 세로(열) 검사
    for j in range(MATRIX):  # 열 고정
        for length in range(1, MATRIX):    # 직선 회문의 최대 길이는 행렬의 길이
            for i in range(MATRIX - length + 1):  # 행 순회
                word = ''  # slicing이 어려우므로 빈 문자열에
                for k in range(length):  # 주어진 회문 길이만큼 순회하면서
                    word = word + matrix[i + k][j]  # 회문인지 확인할 문자열 생성
                if is_palindrome(word):  # 회문인지 확인
                    max_len = max(max_len, length)

    return max_len
'''
전반적인 틀은 회문1과 동일합니다.
하지만 회문1은 찾아야 하는 팰린드롬의 길이를 제공한 반면,
회문2 문제에서 찾아야 하는 답은 회문의 '최대 길이'이기에
회문의 길이는 1이 될 수도, 행렬의 길이인 100이 될 수도 있습니다.
이에 행 검사면 행 고정 후, 열 검사면 열 고정 후
length를 1부터 전체길이까지 순회하면서 검사해야 회문 길이의 최댓값을 구할 수 있습니다.
'''


def main():
    TEST = 10
    MATRIX = 100
    for idx in range(TEST):
        T = int(input())
        table = [list(input()) for _ in range(MATRIX)]

        print(f'#{T} {find_longest_palindrome(table)}')


if __name__ == '__main__':
    main()