# -*- coding:utf-8 -*-
# Author:YEAR
# 避免程序报出未知错误,不要让用户看到错误信息,所以我们需要异常处理
inp = input('hhh:')
try:
    num = int(inp)
    print(num)
except Exception as e:
    print('数据类型转换失败')

# 异常类型,python中异常类型太多了,可以通过except指定需要捕捉哪种异常,而exception可以捕捉所有异常
try:
    num = int(inp)
    print(num)
except ValueError as e:
    print(e)

# except从上到下匹配

# 异常处理完整结构
try:
    pass
except KeyError as e:
    pass
else:
    pass
finally:
    pass

# 主动触发异常
raise Exception('出错了...')

# 断言 没什么屌用 条件成立就成立,不成立就抛异常
assert 1 == 2  # 测试 或者判断程序运行环境
