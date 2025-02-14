num_dict = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9
}


def sort_other_nums(arr):
    arr.sort(key=lambda x: num_dict[x])
    '''
    sort의 key 매개변수 활용
    key 기준으로 sort됨.
    num_dict의 key로 value를 찾아 그 value들로 정렬
    '''
    print(*arr)


def main():
    T = int(input())

    for i in range(T):
        N = input()
        nums = list(input().split())

        print(f'#{i + 1} ', end='')
        sort_other_nums(nums)


if __name__ == '__main__':
    main()
