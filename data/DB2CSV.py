"""
将数据库数据转存为CSV文件
"""
import pandas as pd
import re
import pymysql
from data.ReRepos import ReRepos

# 连接数据库
db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="argudata"
)
base_idx = 1
step = 2000

l1 = []
l2 = []
l3 = []

i = base_idx
while 1:
    select_sql = f"select id_resources,appeal,plea,found from resources where id>={i} and id<{i+step}"
    myCursor = db.cursor()
    myCursor.execute(select_sql)
    res = myCursor.fetchall()
    if len(res) == 0:
        break
    for item in res:
        id_resources = item[0]
        appeal = item[1]
        if len(appeal)<=10:
            l1.append(id_resources)
        plea = item[2]
        if len(plea)<=10:
            l2.append(id_resources)
        found = item[3]
        if len(found)<=10:
            l3.append(id_resources)
    i += step
print(len(l1), len(l2), len(l3))
