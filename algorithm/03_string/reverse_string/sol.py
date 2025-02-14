sentences = [
    'algorithm',
    'life is short',
    'you need python',
    'SSAFY'
]


class reverse_string:
    def __init__(self, test):
        self.test = test
        self.LENGTH = len(self.test)

    def slice_reverse(self):  # slice
        print('0. Slicing')
        for i in range(self.LENGTH):
            print(f'#{i + 1} {self.test[i][::-1]}')
        print()

    def method_reverse(self):           # reverse method
        print('1. Reverse Method')
        reversed_test = self.test[:]    # deep copy 통해 원본 변형 막음
        for i in range(self.LENGTH):
            reversed_test[i] = ''.join(list(reversed(reversed_test[i])))
            print(f'#{i + 1} {reversed_test[i]}')
        print()

    def loop_reverse(self):         # for loop
        print('2. for loop')
        for idx, word in enumerate(self.test):  # enumerate를 사용해서 출력 쉽게
            word = list(word)   # 불변 객체인 str을 list로 변환
            LENGTH = len(word)
            for i in range(LENGTH // 2):    # 한 문장 길이의 절반까지만 for문 순회
                word[i], word[LENGTH - 1 - i] = word[LENGTH - 1 - i], word[i]   # 문자 swap

            print(f'#{idx + 1} {"".join(word)}')


if __name__ == '__main__':
    res = reverse_string(sentences)
    res.slice_reverse()
    res.method_reverse()
    res.loop_reverse()
