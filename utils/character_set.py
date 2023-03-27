def to_char(num):
    character = ''
    if num < 10:
        character = str(num)
    if 10 <= num <= 36:
        if num == 24:
            character = 'Ñ'
        elif num >= 25:
            character = chr(num + 54)
        else:
            character = chr(num + 55)
    elif 37 <= num <= 63:
        if num == 51:
            character = 'ñ'
        elif num >= 52:
            character = chr(num + 59)
        else:
            character = chr(num + 60)
    return character


def character_representation(num):
    if num > 63:
        result = '' + '-'
        for _ in range(num // 63):
            result += to_char(num % 63)
        result += '-'
        return result
    return to_char(num)


def convert(num, base, result=''):
    if num < base:
        return character_representation(num ) + result
    else:
        return convert(num // base, base, character_representation(num % base) + result)