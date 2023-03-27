import re as regex


def pattern_reader(n):
    patterns = [regex.compile('[0-9]'), regex.compile('[a-z]'), regex.compile('[A-Z]'), regex.compile('[ñÑ]')]
    temp = 0
    for i in patterns:
        if i.fullmatch(n) is not None:
            if n in {'Ñ', 'ñ'}:
                temp = 25 if temp == 'Ñ' else 52
                break
            temp = get_character_value(n, patterns.index(i))
    return temp


def get_character_value(num, type_conversion):
    value = 0
    if type_conversion == 0:
        value = num
    elif type_conversion == 1:
        value = ord(num) - 60 if ord(num) <= 110 else ord(num) - 59
    elif type_conversion == 2:
        value = ord(num) - 55 if ord(num) <= 78 else ord(num) - 54
    elif type_conversion == 3:
        value = (63 * num[1]) + pattern_reader(num[0])
    return int(value)


def get_number_base(num):
    base = 0
    i = 0
    while i < len(num):
        temp = pattern_reader(num[i])
        if num[i] == '-':
            count = 1
            char_ex = ''
            for k in num[i + 1:]:
                if k == '-':
                    break
                count += 1
                char_ex = k
            i += count
            temp = get_character_value([char_ex, count - 1], 3)
        if base <= temp:
            base = temp
            base += 1
        i += 1
    return base


def to_base10(num, base):
    result = 0
    i = 0
    while i < len(num):
        temp = pattern_reader(num[i])
        if num[i] == '-':
            count = 1
            char_ex = ''
            for k in num[i + 1:]:
                if k == '-':
                    break
                count += 1
                char_ex = k
            i += count
            temp = get_character_value([char_ex, count - 1], 3)
        result += temp * (base ** (len(num) - i - 1))
        i += 1
    return result