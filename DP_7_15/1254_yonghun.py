# -*- encoding: utf-8 -*-


def palindrome(index, length, str):
    i = 0
    while index + i < length - i - 1:
        if str[index + i] != str[length - i - 1]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    str = input()
    length = len(str)
    answer = 0

    for i in range(length):
        if palindrome(i, length, str):
            answer = length + i
            break

    print(answer)

# Manacher's algorithm : https://algospot.com/wiki/read/Manacher's_algorithm
