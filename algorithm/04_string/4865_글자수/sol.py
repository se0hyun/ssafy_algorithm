def count_word(str1, str2):
    N, M = len(str1), len(str2)
    result = [0 for _ in range(N)]

    for i, char in enumerate(str1):     # result 배열에 인덱스로 저장하기 위해 enumerate 사용
        for j in range(M):      # str2 전체 순회
            if char in str2[j]:     # str1의 글자 하나가 str2에 존재하는지 하나씩 확인
                result[i] += 1      # 존재할 때 마다 배열 값 증가

    return max(result)


def main():
    T = int(input())

    for idx in range(T):
        str1 = input()
        str2 = input()

        print(f'#{idx + 1} {count_word(str1, str2)}')


if __name__ == '__main__':
    main()
