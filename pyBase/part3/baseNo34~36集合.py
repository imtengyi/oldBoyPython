# -*- coding:utf-8 -*-
# Author:YEAR

# 1.1set 无序,不重复序列 {}创建,直接写元素
set1 = {'year', 'jiujiujiu'}
print(type(set1))
# 1.2set功能 __init__()构造方法,,使用强制转换就会调用此方法
# 创建集合
s = set()  # 创建空集合
li = [11, 22, 11, 22]
s = set(li)
# 操作集合
s1 = set()
s1.add(123)  # 添加元素
s1.clear()  # 清空set
s2 = s1.copy()  # 浅拷贝
s1.difference(s2)  # s1中存在s2中不存在的元素
s1.symmetric_difference(s2)  # 对称差集 去掉两个set中相同的元素
s1.difference_update(s2)  # 同difference 不过会更新s1
s1.symmetric_difference_update(s2)  # 同symmetric_difference 不过会更新s1
s1.discard(1111)  # 移除指定元素 不存在不报错
s1.remove(1111)  # 移除指定元素 不存在报错
s1.pop()  # 移除随机元素并且获取此元素
s1.intersection(s2)  # 取交集
s1.intersection_update(s2)  # 取交集并更新
s1.issubset(s2)  # 是否为子序列
s1.issuperset(s2)  # 是否为父序列
s3 = s1.union(s2)  # 取并集
s1.update(s2)  # 接收一个可迭代对象循环调用add()

li = [11, 22, 33]  # list __init__
li()  # list __call__
li[0]  # list __getitem__
li[0] = 123  # list __setitem__
del li[1]  # list __delitem__

# 1.3set小练习 更新字典
old_dic = {
    '#1': 4,
    '#2': 4,
    '#4': 2,
}
new_dic = {
    '#1': 4,
    '#2': 4,
    '#3': 2,
}
new_set = set(new_dic.keys())
old_set = set(old_dic.keys())

remove_set = old_set.difference(new_set)
add_set = new_set.difference(old_set)
update_set = new_set.intersection(old_set)
