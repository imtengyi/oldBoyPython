# -*- coding:utf-8 -*-
# Author:YEAR

# 字符串格式化
# 占位符 %s %d 远远没有这么简单
print("%shahaha%d" % ("ddd", 3))
# %[(name)][flags][width].[precision]typecode
print("%(name)shahaha%(age)d" % {'name': 'alex', 'age': 123})
# flags + 右对齐 正数加号 负数剑豪 -左对齐 正数无符号 负数减号 空格 正数前加空格 负数加减号 右对齐 0 右对齐 正数前无符号 负数前加负号 用0填充空白
print("aaa%(name)+10shahaha %(age)+10d" % {'name': 'year', 'age': 100})
# width 占有宽度
# .precision 小数点后保留的位数
# typecode s r,,返回__repr__ c,,整数将数字换成unicode对应的值 o,,转换成八进制 x,,转换成十六进制 d,,十进制 f,,浮点数 e,,E,,科学计数法,,大小写e g,,G,,超过6位自动转换成科学计数法..自动转换成浮点
# 注意 当字符串没有用到占位符时 %直接用 但是一旦有一个占位符时就必须用%%来表示%



# 更厉害的format字符串格式化   [[fill]align][sign][#][0][width][,][.precision][type]
# fill 填充字符 只能一个字符
# align 对齐方式 需要配合width使用 < 左对齐 >右对齐 =内容右对齐将符号放置在填充字符左侧只对数字有效 ^内容居中
# sign 有无符号数字 +正号加正负号加负号 -正好不变负号加负 空格,正号空格负号加负
# 加# 对于二进制八进制十六进制如果加上# 会显示0b 0o 0x 否则不显示
# %号 会自动将你给的数转换成百分比
# 剩下的和占位符一样
s1 = "======{:*^20s}------{:+d}-----{:#b}".format('year', 123, 15)

# 常用举例
tpl = "i am {},age{},{}".format("seven", 18, 'year')
tpl = "i am {},age{},{}".format(*["seven", 18, 'year'])
tpl = "i am {0},age{1},{0}".format("seven", 18)
tpl = "i am {0},age{1},{0}".format(*["seven", 18])
tpl = "i am {name},age{age},{name}".format(name="seven", age=18)
tpl = "i am {name},age{age},{name}".format(**{'name': "seven", 'age': 18})
tpl = "i am {0[0]},age{0[1]},{0[2]}".format([1, 2, 3])
tpl = "i am {:s},age{:d},{:s}".format('aaa', 123, 'asdfsdf')
tpl = "i am {:s},age{:d},{:s}".format(*['aaa', 123, 'asdfsdf'])
tpl = "i am {name:s},age{age:d},{name:s}".format(**{'name': 'asdf', 'age': 123})
tpl = "i am {name:s},age{age:d},{name:s}".format(name='asdf', age=123)
tpl = "numbers:{:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 0.12)
tpl = "numbers:{0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
tpl = "numbers:{num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
