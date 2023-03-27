from utils.numberrep import NumberRep
from utils.number_set import get_number_base, to_base10
from utils.character_set import convert


def op_info(n, base):
    return [n % base, n // base]


def to_list(num):
    i = 0
    temp = []
    while i < len(num):
        if num[i] != '-':
            temp.append(NumberRep(get_number_base(num[i]) - 1))
        else:
            count = 0
            char_ex = ''
            for k in num[i + 1:]:
                if k == '-':
                    break
                count += 1
                char_ex = k
            temp.append(NumberRep(get_number_base(char_ex) - 1, count))
            i += count + 1
        i += 1
    return temp


def addition(num1, num2, base):
    num1 = to_list(num1)
    num2 = to_list(num2)
    result = ''
    carry = 0
    if len(num1) == len(num2):
        g_num = num1
        l_num = num2
    else:
        g_num = num1 if len(num1) > len(num2) else num2
        l_num = num1 if len(num1) < len(num2) else num2
    while len(g_num) > len(l_num):
        l_num.insert(0, NumberRep('0', 0))
    g_num.reverse()
    l_num.reverse()
    for i in range(len(g_num)):
        sum = g_num[i].value() + l_num[i].value() + carry
        if sum >= base:
            carry = op_info(sum, base)[1]
            sum = op_info(sum, base)[0]
        else:
            carry = 0
        result += str(NumberRep(sum).__str__())
    if carry > 0:
        result += str(NumberRep(carry).__str__())
    return result[::-1]


def subtraction(num1, num2, base):
    num1 = to_list(num1)
    num2 = to_list(num2)
    result = ''
    if len(num1) == len(num2):
        g_num = num1
        l_num = num2
    else:
        g_num = num1 if len(num1) > len(num2) else num2
        l_num = num1 if len(num1) < len(num2) else num2
    if len(num1) < len(num2):
        return 'No se puede realizar la operación'
    while len(g_num) > len(l_num):
        l_num.insert(0, NumberRep('0'))
    g_num.reverse()
    l_num.reverse()
    for i in range(len(g_num)):
        if g_num[i].value() < l_num[i].value():
            subcount = i + 1
            while g_num[subcount].value() == 0:
                subcount += 1
            g_num[i].char = base + g_num[i].value()
            g_num[subcount].char = g_num[subcount].value() - 1
        sub = g_num[i].value() - l_num[i].value()
        result += str(NumberRep(sub).__str__())
    return result[::-1]


def multiplication(num1, num2, base):
    num1 = to_list(num1)
    num2 = to_list(num2)
    num1.reverse()
    num2.reverse()
    carry = 0
    result = ''
    for i in range(len(num2)):
        tempo = result
        result = ''
        for j in range(len(num1)):
            mul = (num2[i].value() * num1[j].value()) + carry
            if mul >= base:
                carry = op_info(mul, base)[1]
                mul = op_info(mul, base)[0]
            else:
                carry = 0
            result += str(NumberRep(mul).__str__())
        if carry > 0:
            result += str(NumberRep(carry).__str__())
            carry = 0
        result = result[::-1]
        if i > 0:
            for _ in range(i):
                result += '0'
        result = addition(result, tempo, base)
    return result


def division(num1, num2, base):
    result = str(to_base10(num1, base) / to_base10(num2, base))
    if '.' in result:
        result = result[:result.index('.')]
    result = convert(int(result), base)
    return result
