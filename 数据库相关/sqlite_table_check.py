# 脚本名称：sqlite_table_check.py
# 作者：Craig Richards
# 创建时间：2013年6月7日
# 版本：1.0
# 修改：
# 描述：检查主 SQLITE 数据库以确保所有表都应存在


import os
import sqlite3

dropbox = os.getenv("dropbox")
config = os.getenv("my_config")
dbfile = "Databases\jarvis.db"
listfile = "sqlite_master_table.lst"
master_db = os.path.join(dropbox, dbfile)
config_file = os.path.join(config, listfile)
tablelist = open(config_file, "r")

conn = sqlite3.connect(master_db)
cursor = conn.cursor()
cursor.execute("SELECT SQLITE_VERSION()")
data = cursor.fetchone()

if str(data) == "(u'3.6.21',)":
    print("\n当前 " + master_db + " 正在使用的 SQLite 版本为：%s" % data + " - 正常 -\n")
else:
    print("\n数据库与主版本不同 - !!!!! \n")
conn.close()

print("\n正在检查 " + master_db + " 是否与 " + config_file + " 匹配\n")

for table in tablelist.readlines():
    conn = sqlite3.connect(master_db)
    cursor = conn.cursor()
    cursor.execute(
        "select count(*) from sqlite_master where name = ?", (table.strip(),)
    )
    res = cursor.fetchone()

    if res[0]:
        print("[+] 表格 : " + table.strip() + " 存在 [+]")
    else:
        print("[-] 表格 : " + table.strip() + " 不存在 [-]")
