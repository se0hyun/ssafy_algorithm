import sys
sys.stdin = open('sample_input.txt')


def compare_string(str1, str2):
    N, M = len(str1), len(str2)
    count = 0

    for i in range(M - N + 1):
        for j in range(N):
            if str1[j] != str2[i]:      # 다른 문자면
                # j = 0           # 첫 번째 문자열의 인덱스를 0으로 조정
                break           # 안 쪽 반복문 탈출
            else:               # 같은 문자일 경우
                if j == N - 1:  # 현재 인덱스가 첫 번째 문자열 끝일 경우,
                    return 1  # 전체가 포함된 것을 확인했기 때문에 1 반환
                elif j != N-1:            # 끝이 아닐 경우 두번째 문자열 인덱스 증가
                    i += 1
    return count


def main():
    T = int(input())

    for idx in range(T):
        str1 = input()
        str2 = input()

        print(f'#{idx + 1} {compare_string(str1, str2)}')


if __name__ == '__main__':
    main()
