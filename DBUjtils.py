import pymysql
host="localhost"
user="root"
password="123456"
database="建设银行"
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def find(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    cursor.close()
    con.close()
# f=open("a","r+",encoding="UTF-8")
# list = f.readlines()
# for i in list:
#     list1 = i.replace("\n","").split(",")
#     sql="insert into user values(%s,%s,%s)"
#     param = [list1[0],list1[1],list1[2]]
#     update(sql, param)




# sql = "select sum(净资产) from user"
# param = []
# data = find(sql,param)
# sum=data[0][0]
# print("总和为：",sum)





# f = open("names.txt","w+",encoding="utf-8")
# sql="select * from user"
# param = []
# data = find(sql,param)
# for i in data:
#     string = ""
#     string = string + i[0]
#     string = string + "," + str(i[1])
#     string = string + "," + str(i[2])
#     f.write(string + "\n")
# f.close()

























