cnt = 0


def itoa(tc, integer_value):
    '''
    itoa란
    정수형으로 입력된 입력값을 str형으로 바꿔주는 C언어 계열의 함수
    즉, 출력은 동일해 보이나 타입이 각각 int, str로 다름. (C의 경우 char)
    ASCII 코드를 활용해 해당 함수를 파이썬에서도 구현 가능

    음수를 지정하는 ASCII 코드는 없으므로 다시 붙여줘야 함
    '''

    is_negative = integer_value < 0  # 입력값이 음수인지 확인

    if is_negative:
        integer_value = -integer_value  # 음수는 양수로 변경

    '''
    0의 ASCII: 48, 1의 ASCII: 49, 2의 ASCII: 50 ...
    이를 활용하면 0~9의 ASCII 코드를 쉽게 구할 수 있음.
    ex) 8의 ASCII 코드: str(48 + 8)
    
    !! 0의 ASCII코드 정도는 외워두면 시험에서 쓸 일 多!!
    '''

    result = ''  # 결과 저장할 빈 문자열
    while integer_value > 0:  # 입력값을 계속 10으로 나눈 몫을 사용할 예정이므로 (0보다 클 동안)이라는 조건문 사용
        remainder = integer_value % 10  # 10으로 나눈 나머지 == 1의 자리 숫자만 추출
        result = chr(48 + remainder) + result  # 1의 자리 추출 후 str형으로 변경 및 기존 result와 합침
        integer_value //= 10  # 10으로 나눈 몫 == 1의 자리만 뺀 숫자

    '''
    Example) 5634, result = ''
    5634 % 10 = 4
    result = str(4) + result    -> result = 4
    5634 // 10 = 563
    
    563 % 10 = 3
    result = str(3) + result   -> result = 34
    563 // 10 = 56
    ...
    '''

    if is_negative:  # 음수 입력값은 다시 '-'를 붙여줌
        result = '-' + result

    print(f'#{tc + 1} {result} {type(result)}')


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        if N == 0:  # 0이 입력될 경우 main 종료
            print(0)
        else:
            itoa(i, N)


if __name__ == '__main__':
    main()
