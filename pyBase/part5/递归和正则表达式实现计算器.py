# -*- coding:utf-8 -*-
# Author:YEAR
import re


def compute_mul_div(arg):
    """
    处理乘除
    :param arg:表达式
    :return:运算结果
    """

    val = arg[0]
    mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val)
    if not mch:
        return
    content = mch.group()

    if len(content.split('*')) > 1:
        n1, n2 = content.split('*')
        value = float(n1) * float(n2)
    else:
        n1, n2 = content.split('/')
        value = float(n1) / float(n2)

    before, after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before, value, after)
    arg[0] = new_str
    compute_mul_div(arg)


def compute_add_sub(arg):
    """
    操作加减
    :param arg:表达式
    :return:计算结果
    """
    while True:
        if arg[0].__contains__('+-') or arg[0].__contains__("++") or arg[0].__contains__('-+') or arg[0].__contains__(
                '--'):
            arg[0] = arg[0].replace('+-', '-')
            arg[0] = arg[0].replace('++', '+')
            arg[0] = arg[0].replace('-+', '-')
            arg[0] = arg[0].replace('--', '+')
        else:
            break

    if arg[0].startswith('-'):
        arg[1] += 1
        arg[0] = arg[0].replace('-', '&')
        arg[0] = arg[0].replace('+', '-')
        arg[0] = arg[0].replace('&', '+')
        arg[0] = arg[0][1:]
    val = arg[0]
    mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val)
    if not mch:
        return
    content = mch.group()
    if len(content.split('+')) > 1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)

    before, after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before, value, after)
    arg[0] = new_str
    compute_add_sub(arg)


def compute(expression):
    """
    操作加减乘除
    :param expression:表达式
    :return: 计算结果
    """

    inp = [expression, 0]

    compute_mul_div(inp)

    compute_add_sub(inp)
    if divmod(inp[1], 2)[1] == 1:
        result = float(inp[0])
        result = result * -1
    else:
        result = float(inp[0])
    return result


def exec_bracket(expression):
    """
    递归处理括号并计算
    :param expression:表达式
    :return: 最终计算结果
    """
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression):
        final = compute(expression)
        return final

    content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression).group()
    before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.*\d*){2,}\)', expression, 1)

    print('before：', expression)
    content = content[1:len(content) - 1]

    ret = compute(content)

    print('%s=%s' % (content, ret))
    expression = "%s%s%s" % (before, ret, after)
    print('after：', expression)
    print("=" * 10, '上一次计算结束', "=" * 10)

    return exec_bracket(expression)


if __name__ == "__main__":
    inpp = "1-2*-30/-12*(-20+200*-3/-200*-300-100)"
    inpp = re.sub('\s*', '', inpp)
    result = exec_bracket(inpp)
    print(result)
