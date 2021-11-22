"""
将数据库数据转存为CSV文件
appeal 字段没有空
plea字段3500左右的空
found 字段 2 个空
appeal and found 没有同时为空的
"""
import pandas as pd
import re
import pymysql
from data.ReRepos import ReRepos

# 连接数据库
def getDB():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="argudata"
    )

def get_argu_1():

    db = getDB()
    base_idx = 1
    step = 2000
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
            plea = item[2]
            found = item[3]

        i += step
