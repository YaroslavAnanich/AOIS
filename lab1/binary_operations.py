import numpy
import ieee754


def direct_code(number):
    direct = numpy.empty(8, dtype=object)
    if number < 0:
        direct[0] = 1
        number = abs(number)
    else:
        direct[0] = 0
    if abs(number) >= 127:
        for i in range(7, -1, -1):
            direct[i] = number % 2
            number //= 2
        return direct
    else:
        for i in range(7, 0, -1):
            direct[i] = number % 2
            number //= 2
    return direct


def inverse_code(direct):
    if direct[0] == 1:
        for i in range(7, 0, -1):
            if direct[i] == 0:
                direct[i] = 1
            else:
                direct[i] = 0
    return direct


def additional_code(inverse):
    if inverse[0] == 1:
        for i in range(7, 0, -1):
            if inverse[i] == 0:
                inverse[i] = 1
                return inverse
            else:
                inverse[i] = 0
    return inverse


def additional_sum(additional1, additional2):
    sum = direct_sum(additional1, additional2)
    if sum[0] == 1:
        inverse_code(sum)
        additional_code(sum)
    return sum


def direct_sum(direct1, direct2):
    sum = numpy.empty(8, dtype=object)
    transfer = 0
    for i in range(7, -1, -1):
        discharge = direct1[i] + direct2[i] + transfer
        if discharge == 0:
            transfer = 0
            sum[i] = 0
        if discharge == 1:
            transfer = 0
            sum[i] = 1
        if discharge == 2:
            transfer = 1
            sum[i] = 0
        if discharge == 3:
            transfer = 1
            sum[i] = 1
    return sum


def additional_subtraction(additional1, additional2):
    if additional2[0] == 1:
        for i in range(7, 0, -1):
            if additional2[i] == 1:
                additional2[i] = 0
                break
            else:
                additional2[i] = 1
        additional2 = inverse_code(additional2)
        additional2[0] = 0
    else:
        if_zero = True
        for i in additional2:
            if i == 1:
                if_zero = False
        if if_zero:
            return additional_sum(additional1, additional2)
        additional2[0] = 1
        additional2 = inverse_code(additional2)
        additional2 = additional_code(additional2)
    return additional_sum(additional1, additional2)


def moving(index, direct):
    result_of_moving = numpy.zeros(8, dtype=object)
    result_of_moving[0] = direct[0]
    for i in range(7, 1, -1):
        result_of_moving[i - index] = direct[i]
    return result_of_moving


def direct_multiplication(direct1, direct2):
    result_of_multiplication = numpy.zeros(8, dtype=object)

    for i in range(7, 0, -1):
        if direct2[i] == 1:
            result_of_multiplication = direct_sum(result_of_multiplication, moving(7 - i, direct1))
    if direct1[0] == 1 and direct2[0] == 1:
        result_of_multiplication[0] = 0
    if direct1[0] == 1 and direct2[0] == 0:
        result_of_multiplication[0] = 1
    if direct1[0] == 0 and direct2[0] == 1:
        result_of_multiplication[0] = 1
    if direct1[0] == 0 and direct2[0] == 0:
        result_of_multiplication[0] = 0
    return result_of_multiplication


def comparison_less(direct1, direct2):
    if int(''.join(map(str, direct1))) < int(''.join(map(str, direct2))):
        return True
    else:
        return False


def decimal_to_binary(number, precision=5):
    binary_str = format(number, '0{}b'.format(precision))
    return binary_str


def binary_division(dividend, divisor):
    dividend_int = ''.join(map(str, dividend))
    dividend_int = dividend_int.lstrip('0')
    divisor_int = ''.join(map(str, divisor))
    divisor_int = divisor_int.lstrip('0')
    dividend_int = int(dividend_int, 2)
    divisor_int = int(divisor_int, 2)
    quotient = 0
    remainder = 0
    for i in range(len(dividend)):
        remainder = (remainder << 1) | int(dividend[i])
        if remainder >= divisor_int:
            remainder -= divisor_int
            quotient = (quotient << 1) | 1
        else:
            quotient = quotient << 1
    quotient_bin = decimal_to_binary(quotient)
    remainder_bin = decimal_to_binary(remainder)
    return quotient_bin, remainder_bin

def float_to_binary(num):
    if num == 0:
        return '0'

    num = abs(num)

    integer_part = int(num)

    decimal_part = num - integer_part
    if integer_part != 0:
        binary_integer = ''.join(map(str, direct_code(integer_part)))
        binary_integer = binary_integer.lstrip('0')
    else:
        binary_integer = '0'
    binary_decimal = ''
    while decimal_part > 0:
        decimal_part *= 2
        if decimal_part >= 1:
            binary_decimal += '1'
            decimal_part -= 1
        else:
            binary_decimal += '0'
    print('binary: ' + binary_integer + '.' + binary_decimal)
    return binary_integer + '.' + binary_decimal


def normalize_binary(binary_num):
    dot_position = binary_num.index('.')
    exponent = dot_position - 1
    normalized_num = binary_num.replace('.', '')
    normalized_num = normalized_num[:1] + '.' + normalized_num[1:]
    return normalized_num, exponent


def binary_to_ieee754(binary_num):
    normalized_number, exponent = normalize_binary(binary_num)
    binary_exponent = ''.join(map(str, direct_code(exponent + 127)))
    binary_mantissa = normalized_number[2:]
    while len(binary_mantissa) != 23:
        binary_mantissa = binary_mantissa + '0'
    ieee754_number = ieee754.IEEE754Number(binary_exponent, exponent, binary_mantissa)
    return ieee754_number


def normalize_ieee754_mantissa(mantissa, difference_exponent):
    normalize_mantissa = mantissa.replace('.', "")
    for i in range(0, difference_exponent-1):
        normalize_mantissa = '0' + normalize_mantissa
    normalize_mantissa = '.' + normalize_mantissa
    normalize_mantissa = '0' + normalize_mantissa
    return normalize_mantissa


def string_to_numpy(mantissa):
    mantissa_index = len(mantissa) - 1
    mantissa_numpy = numpy.zeros(8, dtype=object)
    for i in range(7, 7 - len(mantissa), -1):
        mantissa_numpy[i] = int(mantissa[mantissa_index])
        mantissa_index -= 1
    return mantissa_numpy


def mantissa_sum(mantissa_first, mantissa_second):
    mantissa_first_integer = mantissa_first[0]
    mantissa_second_integer = mantissa_second[0]
    mantissa_first_decimal = mantissa_first[2:8]
    mantissa_second_decimal = mantissa_second[2:8]
    mantissa_first_integer = string_to_numpy(mantissa_first_integer)
    mantissa_second_integer = string_to_numpy(mantissa_second_integer)
    mantissa_first_decimal = string_to_numpy(mantissa_first_decimal)
    mantissa_second_decimal = string_to_numpy(mantissa_second_decimal)
    mantissa_integer_sum = additional_sum(mantissa_first_integer, mantissa_second_integer)
    mantissa_decimal_sum = additional_sum(mantissa_first_decimal, mantissa_second_decimal)
    the_transitional_part = numpy.zeros(8, dtype=object)
    the_transitional_part[7] = mantissa_decimal_sum[1]
    mantissa_integer_sum = additional_sum(mantissa_integer_sum, the_transitional_part)
    mantissa_integer_sum = ''.join(map(str, mantissa_integer_sum))
    mantissa_integer_sum = mantissa_integer_sum.lstrip('0')
    mantissa_decimal_sum = ''.join(map(str, mantissa_decimal_sum))
    mantissa_decimal_sum = "" + mantissa_decimal_sum[2:]
    mantissa_sum_result = mantissa_integer_sum + '.' + mantissa_decimal_sum
    return mantissa_sum_result


def ieee754_sum(ieee_first :ieee754.IEEE754Number, ieee_second :ieee754.IEEE754Number):
    if int(ieee_first.mantissa) > int(ieee_second.exponent):
        mantissa_first = '1.' + ieee_first.mantissa
        mantissa_second = '1.' + ieee_second.mantissa
        difference_exponent = ieee_first.exponent - ieee_second.exponent
        mantissa_second = normalize_ieee754_mantissa(mantissa_second, difference_exponent)
        mantissa_sum_result = mantissa_sum(mantissa_first, mantissa_second)[2:]
        while len(mantissa_sum_result) != 23:
            mantissa_sum_result = mantissa_sum_result + '0'
        iee754_sum_result = ieee754.IEEE754Number(ieee_first.binary_exponent, ieee_first.exponent, mantissa_sum_result)
        iee754_sum_result.print_info()








