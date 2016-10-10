# -*- coding:utf-8 -*-
# Author:YEAR
import json


def fetch(backend):
    result = []
    with open('ha.conf', 'r', encoding='utf-8') as f:
        flag = False
        for line in f:
            if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                flag = True
                continue
            if flag == True and line.strip().startswith("backend"):
                break
            if flag and line.strip():
                result.append(line.strip())
    return result


# 先实现简单的逻辑在再写复杂的逻辑
def add(backend, record):
    record_list = fetch(backend)
    if not record_list:
        # backend 不存在
        with open('ha.conf', 'r') as old, open('new.conf', 'w')as new:
            for line in old:
                new.write(line)
                new.write("\nbackend " + backend + "\n")
                new.write(" " * 8 + record + "\n")
    else:
        # backend存在
        if record in record_list:
            # record 已经存在
            import shutil
            shutil.copy("ha.conf", 'new.conf')
        else:
            # backend存在,record不存在
            record_list.append(record)
            with open('ha.conf', 'r') as old, open('new.conf', 'w') as new:
                flag = False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend " + backend:
                        flag = True
                        new.write(line)
                        for new_line in record_list:
                            new.write(" " * 8 + new_line + "\n")
                    if flag == True and line.strip().startswith("backend"):
                        flag = False
                        new.write(line)
                        continue
                    if not flag and line.strip():
                        new.write(line)
        pass


fetch("biubiubiubiu")
# 利用json把字符串转换为对象
r = input("input:")
# r like this: {"backend":"biu.year.org","record":{"server":"192.168.0.1","weight":20,"maxconn":30}}
dic = json.loads(r)
bk = dic['backend']
rd = "server %s %s weight %d maxconn %d" % (
    dic['record']['server'], dic['record']['server'], dic['record']['weight'], dic['record']['maxconn'])
