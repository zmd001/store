import random
import pymysql
# 银行的名称
bank_name = "北京市建设银行昌平支行"

# 银行的库
users = {}

'''
{"张三":
    {account:"12345",
    "国家":"中国"}
}
'''

"""
1.连接数据库
2.插入数据
"""

# 欢迎界面
''' 
welcome = 
*********************************
*    欢迎来到中国工商银行管理系统 *
*********************************
*    1.开户                      *
*    2.存钱                      *
*    3.取钱                      *
*    4.转账                      *
*    5.查询                      *
*    6.bye！                     *
*********************************
'''

# 专门来获取8位随机账号
def getRandom():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    # 循环8次
    string = ""
    for i in range(8):  # 循环8次获取随机字符
        ch = li[random.randint(0, 9)]
        string = string + str(ch)
    return string

#查看是否存在用户
def user(username):
    # 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
    # 建立游标
    cursor = con.cursor()
    # 增加
    sql = "select 姓名 from 用户表  where 姓名=(%s)"
    param = [username]
    num = cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()
    if num==1:
        return 2

# 银行的核心开户方法
def bank_addUser(account, username, password, money, country, province, street, door):
    user(username)
    len1 = user(username)
    # 先判断银行库是否已满 ： 100个最大
    # if len(users) >= 100:
    #     return 3
    # elif len1==2:
    #     return 2
    # 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
    # 建立游标
    cursor = con.cursor()
    # 增加
    sql = "select count(姓名) from 用户表"
    nu = cursor.execute(sql)
    num = cursor.fetchall()
    num1=num[0][0]
    con.commit()
    cursor.close()
    con.close()
    if num1>=100:
        return 3
# 可以正常开户：将个人数据存到用户库里
    else:
        # 连接数据库
        con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
        # 建立游标
        cursor = con.cursor()
        # 增加
        sql = "select 姓名 from 用户表 where 姓名=%s"
        param = [username]
        nu = cursor.execute(sql,param)
        num = cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()
        if nu==1:
            return 2
        else:
            users[username] = {
                "account": account,   # 账号
                "password": password,  # 密码
                "money": money,   # 金额
                "country": country,   # 国家
                "province": province,  #省份
                "street": street,   # 街道
                "door": door,   # 门牌号
                "bank_name": bank_name   # 开户行
            }
            database(account, username, password, money, country, province, street, door,bank_name)
            return 1

def bank_savemoney(username, money):
    sun=user(username)
    if sun==2:  # 判断用户里面有没有用户名
        nummoney=usermoney(username)
        nummoney= nummoney + money
        databasemoney(username,nummoney)
        print("存钱成功！！！", "您的账号为:", username, "您的余额为:", nummoney)
        return 1
    else:
        return 2
def usermoney(username):
    # 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
    # 建立游标
    cursor = con.cursor()
    # 修改
    # update 学生表 set sn=%s where 姓名=''
    # 查询
    sql = "select 初始金额 from 用户表 where 姓名= %s"
    param = [username]
    num = cursor.execute(sql, param)
    nummoney=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return nummoney[0][0]

def databasemoney(username,nummoney):
    # 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
    # 建立游标
    cursor = con.cursor()
    #修改
    #update 学生表 set sn=%s where 姓名=''
    #查询
    sql = "update 用户表 set 初始金额=%s where 姓名=%s"
    param = [nummoney,username]
    num = cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()

def query():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    savequery = bank_query(username, password)
    if savequery == 1:
        print()
    elif savequery == 2:
        print("密码输入错误")
    else:
        print("该用户不存在")

def bank_query(username, password):
    # 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
    # 建立游标
    cursor = con.cursor()
    # 修改
    # update 学生表 set sn=%s where 姓名=''
    # 查询
    sql = "select * from 用户表 where 姓名=%s and 取款密码=%s"
    param = [username,password]
    num = cursor.execute(sql, param)
    data=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    if num==1:
        print(data)
        return 1
    elif num==0:
        # 连接数据库
        con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
        # 建立游标
        cursor = con.cursor()
        # 修改
        # update 学生表 set sn=%s where 姓名=''
        # 查询
        sql = "select * from 用户表 where 姓名=%s"
        param = [username]
        num = cursor.execute(sql, param)
        con.commit()
        cursor.close()
        con.close()
        if num==1:
            return 2
    elif num==0:
        # 连接数据库
        con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
        # 建立游标
        cursor = con.cursor()
        # 修改
        # update 学生表 set sn=%s where 姓名=''
        # 查询
        sql = "select * from 用户表 where 姓名=%s"
        param = [username]
        num = cursor.execute(sql, param)
        con.commit()
        cursor.close()
        con.close()
        if num == 0:
            return 3

# 银行的核心取款方法
def bank_withdraw_money(username, password, money):
# 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
    # 建立游标
    cursor = con.cursor()
    # 修改
    # update 学生表 set sn=%s where 姓名=''
    # 查询
    sql = "select * from 用户表 where 姓名=%s and 取款密码=%s"
    param = [username,password]
    num = cursor.execute(sql, param)
    data=cursor.fetchall()

#   if num==1:
    if num==1:
        data1=data[0][3]
        if int(data1)<money:
            return 3
        else:
            sum=data1-money
            # 连接数据库
            con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
            # 建立游标
            cursor = con.cursor()
            # 修改
            # update 学生表 set sn=%s where 姓名=''
            # 查询
            sql = "update 用户表 set 初始金额=%s where 姓名=%s"
            param = [sum,username]
            num = cursor.execute(sql, param)
            con.commit()
            cursor.close()
            con.close()
            print("取款成功！", "用户名为:", username, "您当前的余额为：", sum)
            return 1
    elif num==0:
        # 连接数据库
        con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
        # 建立游标
        cursor = con.cursor()
        # 修改
        # update 学生表 set sn=%s where 姓名=''
        # 查询
        sql = "select * from 用户表 where 姓名=%s"
        param = [username]
        num = cursor.execute(sql, param)
        con.commit()
        cursor.close()
        con.close()
        if num==1:
            return 2
        else:
            return 0
    con.commit()
    cursor.close()
    con.close()

def withdraw_money():
    username = input("请输入用户名：")
    password = input("请输入取款密码：")
    money = int(input("请输入您的取款金额："))
    # 将数据传给银行
    status1 = bank_withdraw_money(username, password, money)
    if status1 == 0:
        print("您输入的账号不存在！")
    elif status1 == 2:
        print("您输入的密码错误！")
    elif status1 == 3:
        print("您的余额不足！")
    elif status1 == 1:
        print("")

def savemoney():
    username = input("请输入用户名:")
    while True:
        money = input("请输入金额:")
        if money.isdigit():
            money = int(money)
            break
        else:
            print("余额输入错误，请重新输入！")
    returnvalue = bank_savemoney(username, money)
    if returnvalue == 1:
        print("")
    else:
        print("查无此用户！！！")

# 普通的开户方法
def addUser():
    # 完成具体的开户输入
    # 姓名(str)、密码(int:6位数字)、地址、存款余额(int)、国家(str)、省份(str)、街道(str)、门牌号(str)
    username = input("请输入姓名：")
    password = input("请输入取款密码：")
    money = int(input("请输入您的初始金额："))  # 金额是整数形式
    print("接下来输入地址信息：")
    country = input("请输入您所在国家：")
    province = input("请输入您所在省份：")
    street = input("请输入您所在的街道：")
    door = input("请输入您地址的门牌号：")
    account = getRandom()  # 获取随机账号

    # 将数据传给银行
    status = bank_addUser(account, username, password, money, country, province, street, door)
    if status == 3:
        print("对不起，银行用户已满！请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请勿重复开户！")
    elif status == 1:
        print("恭喜，开户成功！以下是您的个人开户信息：")
        print("-------------------------------------")
        print("您的账号为:", users[username]["account"])
        print("您的密码为:", users[username]["password"])
        print("您的余额为:", users[username]["money"])
        print("您的用户名为:", username)
        print("您所在国家为:", users[username]["country"])
        print("您所在省份为:", users[username]["province"])
        print("您所在街道为:", users[username]["street"])
        print("您所在门牌号为:", users[username]["door"])
        print("开户行名为:", users[username]["bank_name"])
def write():
    f = open("name.txt", "w+", encoding="utf-8")
    for key in users.keys():
        string = ""
        string = string + key  # 先拼接姓名
        string = string + "," + users[key]["account"]
        string = string + "," + str(users[key]["password"])
        string = string + "," + str(users[key]["money"])
        string = string + "," + users[key]["country"]
        string = string + "," + users[key]["province"]
        string = string + "," + users[key]["street"]
        string = string + "," + users[key]["door"]
        string = string + "," + users[key]["bank_name"]
        # 写入
        f.write(string + "\n")
    f.close()

def bank_transfer(out_username, up_username, out_pass, out_money):
    # 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
    # 建立游标
    cursor = con.cursor()
    # 增加
    sql = "select 姓名 from 用户表 where 姓名=%s"
    param1 = [out_username]
    num1 = cursor.execute(sql, param1)
    con.commit()
    cursor.close()
    con.close()
    # 连接数据库
    con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
    # 建立游标
    cursor = con.cursor()
    # 增加
    sql = "select 姓名 from 用户表 where 姓名=%s"
    param2 = [up_username]
    num2 = cursor.execute(sql, param2)
    con.commit()
    cursor.close()
    con.close()
    if num1==1 and num2==1:
        # 连接数据库
        con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
        # 建立游标
        cursor = con.cursor()
        # 增加
        sql = "select 取款密码 from 用户表 where 姓名=%s"
        param = [out_username]
        num = cursor.execute(sql,param)
        data=cursor.fetchall()
        data1=data[0][0]
        con.commit()
        cursor.close()
        con.close()
        if int(data1)==int(out_pass):
            # 连接数据库
            con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
            # 建立游标
            cursor = con.cursor()
            # 增加
            sql = "select 初始金额 from 用户表 where 姓名=%s"
            param = [out_username]
            num = cursor.execute(sql, param)
            data = cursor.fetchall()
            data2 = data[0][0]
            con.commit()
            cursor.close()
            con.close()
            if data2>=out_money:
                # 连接数据库
                con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
                # 建立游标
                cursor = con.cursor()
                # 增加
                sql = "select 初始金额 from 用户表 where 姓名=%s"
                param = [up_username]
                num = cursor.execute(sql, param)
                data = cursor.fetchall()
                data3 = data[0][0]
                con.commit()
                cursor.close()
                con.close()
                data2=data2-out_money
                data3=data3+out_money
                # 连接数据库
                con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
                # 建立游标
                cursor = con.cursor()
                # 增加
                sql = "update 用户表 set 初始金额=%s where 姓名=%s"
                param = [data2,out_username]
                num = cursor.execute(sql, param)
                con.commit()
                cursor.close()
                con.close()
                # 连接数据库
                con = pymysql.connect(host="localhost", user="root", password="123456", database="建设银行")
                # 建立游标
                cursor = con.cursor()
                # 增加
                sql = "update 用户表 set 初始金额=%s where 姓名=%s"
                param = [data3, up_username]
                num = cursor.execute(sql, param)
                con.commit()
                cursor.close()
                con.close()
                print("转账成功！", "转出账号为:", out_username, "转出账号余额为:", data2, "转入账号为:", up_username,
                      "转入账号余额为:", data3)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1

def transferMoney():
    out_username = input("请输入转出账号:")
    up_username = input("请输入转入账号:")
    out_pass = input("请输入转出账号密码:")
    out_money = int(input("请输入转出的金额:"))

    status5 = bank_transfer(out_username, up_username, out_pass, out_money)
    if status5 == 1:
        print("转出账户或转入账户不存在！")
    elif status5 == 2:
        print("密码不正确！")
    elif status5 == 3:
        print("余额不足！")
    elif status5 == 0:
        print("")

def database(account, username, password, money, country, province, street, door,bank_name):
# 连接数据库
  con = pymysql.connect(host="localhost",user="root",password="123456", database="建设银行")
# 建立游标
  cursor = con.cursor()
# 增加
  sql = "insert into 用户表 value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  param = [account,username,password,money,country,
           province,street,door,bank_name]
  num = cursor.execute(sql,param)
  con.commit()
  cursor.close()
  con.close()

while True:
    print("""*    欢迎来到中国工商银行管理系统 *
*********************************
*    1.开户                      *
*    2.存钱                      *
*    3.取钱                      *
*    4.转账                      *
*    5.查询                      *
*    6.bye！                     *
*********************************
    """)  # 打印欢迎信息
    chose = input("请输入您的业务编号：")
    if chose == "1":
        addUser()
        write()
    elif chose == "2":
        savemoney()
        write()
    elif chose == "3":
        withdraw_money()
        write()
    elif chose == "4":
        transferMoney()
        write()
    elif chose == "5":
        query()
        write()
    elif chose == "6":
        print("退出成功！欢迎下次光临！")
        break
    else:
        print("输入非法！请重新输入！")
